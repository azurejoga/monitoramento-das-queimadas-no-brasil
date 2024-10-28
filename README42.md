# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb2792e4-ace2-3042-8df5-49037c71ed26 | -4.18078 | -46.81224 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 449c5e5d-d1f2-3ad2-a071-451909e90f2e | -4.12935 | -47.32898 | 2024-10-28 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 8c6183c9-56d3-38d8-bcdd-663f7f53d24a | -4.12884 | -46.86409 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89da792f-3eae-3f42-a52f-ddd6862ee138 | -4.12568 | -47.32393 | 2024-10-28 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 801c371c-40b0-38a0-b0a7-cf9c80646589 | -4.12496 | -47.32827 | 2024-10-28 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 18b9ab53-2526-37ef-9a83-347b83157a88 | -4.12422 | -46.89234 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68eaf3bc-bde1-3931-9035-28e6265ffeb5 | -4.12358 | -46.89628 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a6ab09-9fc7-3243-8c49-ed1db54073ed | -4.12131 | -47.32316 | 2024-10-28 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 063970ed-50a4-3dde-8d29-ea7beb7f1433 | -4.12057 | -47.32755 | 2024-10-28 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1531a461-fc63-32b9-9229-2bbf64595c1e | -6.4372 | -47.53543 | 2024-10-28 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81151791-d6e2-317d-9768-df0e1cad8e69 | -6.36461 | -47.91878 | 2024-10-28 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ca267b-1c35-3201-b933-332405df143e | -6.3639 | -47.92307 | 2024-10-28 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86826578-7f2c-3334-a385-2c9a962f644d | -6.07966 | -47.20626 | 2024-10-28 04:06:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b04f3d4-536c-3106-a4ad-38117ed77a35 | -5.78671 | -47.09135 | 2024-10-28 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba964af8-188f-37bf-88bc-b97e8ca8e4a1 | -5.78251 | -47.09065 | 2024-10-28 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e377ba4-0324-3bfc-ba6d-70a28948e7e1 | -5.75078 | -46.51163 | 2024-10-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc3e3442-f80a-3a5d-92e7-1741e99ca3bd | -5.75044 | -46.51186 | 2024-10-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47d5eb82-d474-342f-b878-0b99c433e207 | -5.71374 | -47.11131 | 2024-10-28 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5356dc78-ceeb-36a1-97f6-23bfe585cd85 | -5.71309 | -47.11525 | 2024-10-28 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93253204-9b1a-35aa-9e83-0eb07f15a4fb | -5.32242 | -47.0126 | 2024-10-28 04:06:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae6e55a6-c013-326e-ab29-8d2e0b85e773 | -5.24371 | -46.70168 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd50676b-23e0-3c15-a1e6-45b2117c0436 | -5.2402 | -46.69724 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a4487f-87b5-3b6a-9386-6346b6931692 | -5.23914 | -46.678 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b1a514e-a575-3615-9d5c-083643e9f507 | -5.15354 | -47.70931 | 2024-10-28 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d09214-98ca-395a-b321-f6521c390678 | -5.14429 | -47.01536 | 2024-10-28 04:06:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53658d5e-05c2-36a9-ae76-92bbfe9da082 | -7.63069 | -47.07576 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4d1ba7f-af16-3df2-92a0-3d399bf7af42 | -7.63007 | -47.07943 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8afc2a4-9350-307d-8fe8-70ae0f90bc1c | -7.47605 | -46.90414 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcc4b349-1e62-336f-a604-bf29815a018b | -6.5988 | -47.16102 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e019ad4-8161-3177-9d4e-42f433da6378 | -9.26736 | -47.91135 | 2024-10-28 04:06:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aab6da0-c662-3bc4-8edf-3cb066e59a75 | -9.26318 | -47.91057 | 2024-10-28 04:06:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 841d4722-6880-3105-924f-44e1b3ad03c0 | -9.25899 | -47.9098 | 2024-10-28 04:06:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 816c3da0-3462-35ab-ac88-4a197da97c4e | -8.5481 | -47.9998 | 2024-10-28 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32e5101-d8a5-344b-b78b-e9ab60cb8bc7 | -4.92143 | -49.02074 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 888e9fca-e35e-3f4a-b073-ced2d032fede | -4.91824 | -48.63483 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35af1388-6557-3ffc-90e6-390450982f77 | -4.91658 | -49.01983 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd88eafe-7055-3bd1-927a-5cf1e3df5141 | -4.91351 | -48.634 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcc8a079-7669-3f2d-a126-a0930adb8ec3 | -4.91265 | -48.63908 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14fab617-229f-39d3-adeb-9ef8c6fad74f | -4.90572 | -48.99573 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58f1e1f7-d70c-3697-8c55-6d0dc0741be5 | -4.89586 | -48.65191 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13098a5f-bde8-3e22-b200-806205794d74 | -4.89199 | -48.64599 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e76ddc2-2223-3d9f-80f7-639afcb131b7 | -4.89027 | -48.65615 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df2963b1-c23c-3bf0-94ed-0a199daecb0e | -4.874 | -48.5801 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4950cbd-ea18-3031-a68c-bcc32f0cb8f4 | -4.66574 | -47.89578 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27fcb6f6-a071-3e39-8734-74ab08cea4b8 | -4.57141 | -48.56496 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3269c72-93ca-388b-b1ce-2dd363aaa8ea | -4.487 | -48.11959 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b49abe8e-116c-30eb-8595-dde75667d69c | -4.48622 | -48.12438 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffe5b062-5eec-35cc-a404-84e37f9e942c | -4.48239 | -48.11884 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6f3c698-52e4-3911-9afe-46399a5b8128 | -4.36012 | -48.5936 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 351b7344-be16-3f84-a361-33441ed18db9 | -4.35044 | -48.14879 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc673594-bd0c-3871-a1a8-e93c2beb3445 | -4.34369 | -48.63285 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6c39755-f7b8-3a6e-a9cf-1fe37032353c | -4.33803 | -48.63724 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8223e46e-ed77-3c43-972d-59b3d21ecf33 | -4.33713 | -48.64256 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d1605c3-ebf5-3116-9450-14b83e98a716 | -4.29678 | -48.65042 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0641d1a-764c-3c95-99e2-baaff4af36a6 | -4.29612 | -48.652 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c7279a8-3dbc-324d-9040-4783795fdc7a | -4.29591 | -48.65573 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba80d685-6e8f-35a3-baa9-396fdd5bdcd5 | -4.29236 | -48.61748 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5b38f86-9a47-3e57-9820-111f2f344465 | -4.28843 | -48.61153 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9025537-acbd-330f-96a7-08c4f388f711 | -4.28757 | -48.6167 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 545dcb91-e6ac-32c0-8350-61c579563e2f | -4.24936 | -48.55174 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 641ba972-2ed8-33a2-bcaf-9636f5669c3a | -4.24373 | -48.55606 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c09bc373-ec73-394b-9734-ef7a8144344c | -4.23334 | -48.55957 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0f63518-8952-39b4-ba1b-ef441a24871c | -4.22188 | -48.56745 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de29a105-9633-3387-b91e-6cbdeed8c9c8 | -4.21711 | -48.56664 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3576e9e-8808-383a-83b3-cd318601693e | -4.16727 | -48.60104 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75227b68-95e2-3e6c-bc06-90e1e28721ce | -4.14982 | -48.7661 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca8413e8-6044-3276-ab13-a27fd673c7ee | -4.14674 | -48.75466 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4d1f6f-423c-3a9a-bed1-30a3e083576d | -4.14586 | -48.75999 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4923be3-ca6e-376d-ab6e-1881328f360f | -4.14497 | -48.76535 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fad67896-660f-3d8e-8f27-ff6c7ec605e2 | -4.14191 | -48.75382 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61a0edd4-11d0-34be-8b2f-814863c74a18 | -4.14102 | -48.75919 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f75d38b-c3c9-3ebc-86df-f210e2896576 | -4.14042 | -48.29813 | 2024-10-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eff07a79-3e0d-38b9-80a3-a2273f6172e4 | -4.13876 | -48.29582 | 2024-10-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efdc9115-0496-3d9d-9d30-53fd25040240 | -4.1379 | -48.30112 | 2024-10-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cc6a8ca-8b08-336c-8c3a-0b4dbdb41c79 | -4.09925 | -48.50772 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b639777-53e1-3c93-a7a9-690a6085a6c8 | -4.0984 | -48.51291 | 2024-10-28 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18fc548e-5fa0-3472-bb87-c6eb110cc4bf | -4.0229 | -48.8208 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 744c8deb-38e6-3a5c-abbc-ca0f431007b7 | -4.01804 | -48.81993 | 2024-10-28 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 776f0e34-c8d8-3509-a7b9-13d169ffc989 | -3.92333 | -48.00105 | 2024-10-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04519970-0197-36f3-adcb-d3e8e1703f57 | -5.41966 | -49.2382 | 2024-10-28 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79bf1747-325b-33f9-808e-7fe70dc59a26 | -5.37924 | -48.35244 | 2024-10-28 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09ef3080-3c7c-39e8-bd1f-1bea86c13c0c | -5.22985 | -47.95462 | 2024-10-28 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31108d23-8e88-3e58-be78-0835d20f1a6d | -5.22537 | -47.95378 | 2024-10-28 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6843e77f-0562-3fcc-bb7c-f053bbcbf6bb | -7.95579 | -49.05692 | 2024-10-28 04:06:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fda0215c-418d-3f07-9797-5f407c4fc0fe | -8.13683 | -49.48133 | 2024-10-28 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a332dd17-08dd-3f68-9bb9-a03e63de4969 | -8.13595 | -49.4864 | 2024-10-28 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e48d0bf6-c19e-3195-a1bd-824fc430aee6 | -3.4335 | -50.25274 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd706edd-291f-3a70-9d80-1e5369f95886 | -3.43319 | -50.32096 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7124cc95-826c-3baa-9bc1-4261e34139a4 | -3.43291 | -50.25623 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9579e92e-9bcd-3731-8603-9d86422e7294 | -3.60438 | -49.36044 | 2024-10-28 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24c44b85-171d-3cf2-8a06-e5994fcdd10f | -3.60387 | -49.36352 | 2024-10-28 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10a03fdd-3a49-3dff-99c3-1d465f19932d | -3.59929 | -49.35959 | 2024-10-28 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aeeef2cf-4313-373c-b2f0-21c5212aea10 | -3.59878 | -49.36267 | 2024-10-28 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| decbdd5e-766b-37f0-bfed-809883af0861 | -4.74593 | -50.82835 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d9ced7e-ad9c-3878-8bf4-39906acd62b1 | -4.50396 | -50.75301 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7488c04-d02c-37c3-beaa-c1e227460aee | -4.5034 | -50.75611 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9287299-db2d-3518-8e9f-b9b72e8cd884 | -4.50334 | -50.75657 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 400ae04f-e6b0-38ef-96fa-00f16fb9bb31 | -4.12194 | -50.50445 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4f1763c-b27f-3882-b528-6150c112dbf0 | -4.12135 | -50.50787 | 2024-10-28 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad9e752-155c-326e-b9e8-8627591c428f | -3.67449 | -50.29819 | 2024-10-28 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
