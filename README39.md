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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 731b60ee-935f-3b86-a9be-981566b37561 | -2.6365 | -54.19482 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb6768fe-82fe-324d-b0f1-e4b66993df99 | -3.96111 | -46.88645 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96203990-4204-331a-b820-97897edaf600 | -2.88883 | -54.16021 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f566b23d-6c2b-307d-87b9-8e4e51cfd080 | -3.74313 | -51.84066 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56523838-d23e-3c42-913f-ef463d097abf | -6.46054 | -47.53931 | 2024-12-02 04:25:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c51c690-b4a6-3ecd-b762-5111be662825 | -2.75043 | -51.75318 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 585ec32f-d594-37c4-acdd-50ae927dcd15 | -4.09897 | -46.9478 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4aa7217-6cbc-36d0-a3ef-d95bc40585bc | -2.81599 | -53.95761 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3a1dfa2-34fd-39c7-8296-eddbbed88e7b | -10.65636 | -44.48917 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f91bc1d1-c80b-333d-9b21-218e9894a8c2 | 1.61069 | -50.93853 | 2024-12-02 04:25:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba0dab40-00ea-3a31-aad1-ee65d0339988 | -4.07386 | -46.6827 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb91bbae-bb1d-3075-a926-d99393ea3fc0 | -3.54022 | -51.49622 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d16dfec3-ee11-3aa9-a9d8-c54f7bc0f48d | -3.1276 | -51.12166 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e758c202-db0c-36b9-990e-7e7bc109a1f9 | -4.90994 | -41.33392 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4339a6b3-6401-321f-8574-3ecf18bebf36 | -3.71879 | -51.79799 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78130bdc-eadc-3f94-a576-5b97f45d4039 | -5.11838 | -43.21259 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6222d1ac-cb3d-3e66-b70f-fc1480746b58 | -4.59448 | -50.61005 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e19034d8-29f3-339c-928b-257742b3056e | -3.21562 | -53.13018 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b466941-7d3d-3daf-bca7-4a00af7310c2 | -10.6587 | -44.49778 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f44159cb-63e2-3570-9c38-ff47c4fedc6b | -4.024 | -49.94157 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d772f6-2915-3cf5-aa55-2b592f6e35f8 | -3.93597 | -46.69736 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fdba224-0e88-3e6c-aaaa-aca1907d41d3 | -3.64777 | -50.21235 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bddb6ad1-11c1-33e0-828d-ad0408b8bcea | -4.07333 | -46.81653 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b9a387-e496-3074-a158-54fe17b009e0 | -3.97787 | -46.71479 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2cc3cef-4513-300f-87f7-0ff72174e76a | -4.58432 | -43.35754 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c1a17d22-934d-3cb1-af9d-f0e1f60db417 | -3.74036 | -53.39042 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dfcc837-e54f-3701-859c-1e313304545b | -4.16917 | -48.19656 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a3d5c99-f910-31dc-9f30-a568706bbdf5 | -3.10523 | -54.05025 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6815a9a2-28bf-3523-8823-f41b305530ac | -3.69446 | -47.11641 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37251c61-7113-3eed-a054-2c56b080f417 | -3.78151 | -52.03849 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99f87d27-252a-3a35-b0b0-264e4d80e40a | -4.3193 | -48.09628 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 362bdca0-bf64-31c3-9135-b022e744e3f1 | -2.91228 | -54.11946 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5ba8525-66bd-3b40-b1b9-4404daadef44 | -2.74264 | -51.75409 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 185ccd7b-d859-3f25-95e6-9ecc467a6a68 | -4.53019 | -45.70054 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 417d033d-6198-36e7-b30c-d85895488ed7 | -5.63945 | -51.32308 | 2024-12-02 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e91d1d0-c40e-3e8d-9591-372e65548613 | -3.95748 | -49.75909 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62c3466e-8e1b-3411-a6a6-1764de139732 | -4.19591 | -50.68168 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d11a0463-7136-398b-b121-8c38ce68c58a | -3.48933 | -52.09879 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ee82ec-b725-3e88-842c-366da4300914 | -3.68077 | -51.69887 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dceda9c-8a4c-3139-b96c-a228f4b46b1c | -4.09359 | -44.85685 | 2024-12-02 04:25:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6728b45-d752-3c55-8ede-674a13db87e3 | -3.98123 | -46.73706 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a0cd1c5-1d5d-3b0d-958d-38ebe9c00256 | -5.1737 | -44.80344 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93bb1448-7145-335e-bf82-7d7f0e3412d0 | -3.94827 | -48.1795 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7778b24a-72be-3a52-b1cf-2f56063d1b21 | -2.80672 | -53.06072 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1000b733-2b43-3025-b8ba-75d2bbe23138 | -3.30795 | -53.86748 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66f71960-b750-3cfe-b740-1e179d81ffe7 | -2.81243 | -53.05621 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65c2c962-e881-3763-a975-337b002271de | -3.81678 | -46.67811 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 234acf07-1f41-3421-8bcb-05ad26f2680d | -5.9119 | -45.57952 | 2024-12-02 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a9fe927-4033-317e-8bbd-d4021d188c3d | -4.26399 | -50.84945 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71d1b24b-e1ed-3543-b2f2-5aaa198131ec | -3.58656 | -52.05041 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0296da71-78df-3109-87b0-8f05eb3e1cd6 | -3.3556 | -49.56652 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a9ba8f-6deb-3e99-a6a0-9987685e52d0 | -5.0068 | -44.16847 | 2024-12-02 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38addb31-4f28-3b0e-b3e6-97fd7408b683 | -4.05195 | -50.90338 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db51d92-4d40-3cc9-b11b-aaf380478eb1 | -3.18569 | -51.16314 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dca7249-81d8-3179-89b2-8f9c986ad6ac | -4.64467 | -46.89876 | 2024-12-02 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91a208c8-50f4-3b34-8e78-f6edf82f1517 | 1.93993 | -55.71321 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ada17e-7dd1-3561-80d7-97ffaa94eb03 | -3.05588 | -51.0596 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fe3c90b-b97f-3a97-bdc7-bab2dc26fcec | -3.26243 | -48.89935 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7468c8f0-eb58-3c59-a386-f736aad14ae3 | -3.40047 | -50.23045 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e26629d-8afb-3f3b-b731-05e42f7edc3f | -4.02863 | -49.93749 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8867c8ea-ac70-3d24-989b-de11853b5369 | -2.82327 | -51.34175 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b07b1592-7e60-3a64-b76f-40d92b16a49a | -3.70807 | -52.19121 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d10c4e0-d4c2-3478-9eb8-84c21a51ee14 | -10.65576 | -44.49321 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1331414-ba30-3382-b173-53887a00a5d1 | -2.8107 | -53.06681 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ddbf18f-f938-36b6-b438-d9ae9b6be4a3 | -3.79664 | -46.69664 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444eca6d-7dd3-3224-9393-dd2f81f68e30 | -4.05934 | -46.81791 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2613371c-e7a8-3afc-ae5c-6996a96bbf99 | -4.04156 | -50.73608 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d771f69d-660e-33c1-bcb0-875ce4cd5cf7 | -3.0472 | -49.37333 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e2c76b8-69cd-352f-8dba-468e2b96a788 | -5.6529 | -51.47015 | 2024-12-02 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a11f89-1986-30d9-a356-d39952e28037 | -4.07665 | -46.68673 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2121a75b-6d06-300b-9d86-fd6848308855 | -6.37033 | -47.35346 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4cf2951f-5c4f-32a6-90b1-e02f303d42e6 | -4.00204 | -46.94003 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a1d111-adb4-37bb-b172-d0ac68d5ecc9 | -4.79805 | -44.74577 | 2024-12-02 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ba41a8-0dd8-353b-b3d1-dbd66a778466 | -4.44935 | -47.61895 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4762f936-dcb9-33d1-980b-4b54770fb4c2 | -3.07255 | -49.48083 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f3d727f-1c7a-3414-866f-e4966e671452 | -3.21165 | -53.12423 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48bd7b82-bd4d-368f-959b-8d5d5bff2210 | -6.08304 | -48.05976 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 534d9533-ab39-36db-b60c-8e757ddf97e3 | -3.94653 | -48.89127 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18edc3fd-d655-350e-b71f-77110737c79d | -3.76151 | -46.51842 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6143a660-8a9c-3d25-b4ca-92e76b0b54ed | -3.28551 | -50.78899 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5b00cea-058f-3bff-803a-adefe221ea11 | -5.57712 | -45.14747 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32c335b3-4db2-3fab-9428-5c11c7b59059 | -9.18523 | -45.34971 | 2024-12-02 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e24f8f7d-d7e6-3f13-a2eb-ba89ca8513db | -3.99444 | -46.50152 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1b34814-5413-370d-bbb4-bbf9a32867f3 | -4.07554 | -46.69378 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57239499-8a18-3dca-b29d-679fbd6f3e54 | -4.05666 | -50.95247 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ffc7316-5c0a-3f19-8f9a-d1be70556c6f | -3.09314 | -49.49833 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038cd482-62bd-3491-9e0e-15369cb93a4d | -4.19244 | -50.67757 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04331d23-a472-3a52-96f0-2657c1290743 | -2.8164 | -53.0623 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7c7ecdb-ba2e-378b-a036-91f39b1b9233 | -5.1267 | -43.20572 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 4c3b7003-0f68-36c2-baec-ec589d72af64 | -4.64132 | -46.89824 | 2024-12-02 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 131f8b6a-3379-3620-9462-ceeb550c5627 | -2.99043 | -51.33091 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b1161b2-1b70-397f-a612-3b356ed7e60c | -4.25588 | -50.84804 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d81322f4-cff2-37d6-9a1a-74a0d0706753 | -4.10514 | -46.95243 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0344281c-47d4-3bc1-bbef-fe0897a77a64 | -3.85627 | -47.04597 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0df073ca-cb1a-30af-a7a6-c0879be8150d | -3.11902 | -53.80655 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b155783d-078c-38f6-a7e3-6293a07f7757 | -4.03918 | -46.83651 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b96e528-ac3f-3938-8cb2-eb26fddd31e5 | -5.58326 | -45.15202 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 87fa5499-0efd-3c55-b4ae-f4c158a266ef | -3.09721 | -54.1319 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb21f38-dd54-3043-a113-c1f8d94121ea | -4.05878 | -46.82146 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dfc02a0-76fe-324d-afed-7c0c47f220dd | -3.75633 | -52.27002 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
