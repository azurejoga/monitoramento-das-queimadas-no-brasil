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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60154cc7-f08a-39d6-b626-5da479bea86d | -11.43929 | -55.00871 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe7760a-4f50-30bd-859d-09371f663dfc | -11.45319 | -55.00701 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d0908a-98ff-3e9c-9f81-1f74520deaf2 | -12.53225 | -57.17586 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 008095ec-5efd-3744-9d39-3f616b445805 | -10.62777 | -49.43548 | 2025-06-01 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 836a08aa-0ba2-3d76-bd25-fc9b3f9a4c32 | -11.70969 | -56.44993 | 2025-06-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaa1ae24-ba1f-3ab1-a41f-d344c7ce27f5 | -11.42935 | -55.00711 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be0fdf92-549a-346a-94ab-56b3603db662 | -11.43045 | -55.00008 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33fe1f2e-0a53-34d3-a094-086f371d5969 | -11.91805 | -54.41659 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab73915-0a9c-3fa0-8763-be4447b8f2d1 | -13.09638 | -45.27486 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24fba3b5-0384-38ea-9fc9-95b9be7a12d9 | -13.63483 | -52.18493 | 2025-06-01 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3d52648-b573-3443-96ba-ffe8c5c2492d | -14.64743 | -45.41175 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29786ab3-b2cc-3644-984b-4ec3d7fe5bcc | -12.08638 | -54.57822 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97626dc6-c269-3716-8886-9b25b820b60b | -9.91881 | -59.90813 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ad6eabf-239f-318f-a89b-fc7eede88124 | -10.82491 | -56.95158 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a1fb3ff-7d99-3b1f-aaf6-a7999ff62bfe | -12.52643 | -57.19008 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3d198e3-6095-391c-828e-a7cf253c482d | -9.92738 | -59.90605 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e2715e84-e672-3f02-b0c9-c36b12644932 | -13.10754 | -45.27335 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0fef5c3-b837-3b85-8782-c1aaaabd678d | -11.14204 | -53.9265 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 567b3757-feaa-359f-b9c7-88c6bb2be6ab | -14.68886 | -45.09644 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bbfc265-9835-350b-bbc9-610a9764926d | -11.07928 | -54.7708 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca4427ab-6d30-30b0-93b4-2ba5c2fde4bc | -12.09318 | -54.667 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbf3a139-4635-3f92-b294-b2b9eaee44b5 | -10.83111 | -56.9564 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d43fe405-b301-310e-bcbf-7772fcb4111c | -11.82633 | -51.27282 | 2025-06-01 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c6b8ff0-3cdb-3033-96ee-8405f0a78858 | -12.01654 | -49.52042 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aae5784-048d-3264-afa0-b0ff37b486a3 | -13.10886 | -45.26796 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3acfa667-0cd1-34c6-94d0-39969e61bc36 | -11.0815 | -54.77837 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aaf0f9d-e92b-38e5-b3eb-43b4b26b2005 | -14.57597 | -58.74886 | 2025-06-01 04:57:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78d43a55-abd5-35d0-90ef-df0cccfd3364 | -14.02687 | -55.13251 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ea6af3-85fa-3352-b21f-fa724686ae16 | -11.0721 | -54.77325 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f204baa0-33fe-3edf-b4b2-daafcb6a64be | -14.03241 | -55.14077 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5256df3f-087f-3df2-abb0-ba0d2ae199cf | -10.6813 | -47.19975 | 2025-06-01 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ef005c6-c5e2-3512-a5ea-3e93f1a9f936 | -13.63916 | -52.181 | 2025-06-01 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 720622e2-746c-3bff-ba8a-d8a5508f7a58 | -14.03297 | -55.13718 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fb334a5-7afd-3723-9dc7-8ef38ee6832d | -13.09731 | -45.26667 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e73b8070-be7b-3349-be4f-601c073ed099 | -11.13927 | -53.94458 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcbb3117-97bf-3375-90c0-67cd492be27d | -11.71303 | -56.45048 | 2025-06-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a78779e-0aef-36ff-bee0-5667feaa27ca | -11.08482 | -54.77891 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9df4a7c-b4cf-318a-94e9-68a72b93b635 | -11.44646 | -55.00626 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e178557-a61c-3fb5-82e2-d7de21d00a39 | -12.52704 | -57.18639 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af73d1a1-fe4f-33be-810f-67367ae7b7bd | -11.3665 | -55.12647 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6953f856-e252-30a1-b1da-a0c30c8e7dd5 | -10.46036 | -47.94525 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e42edea-5c98-37b2-ba32-3e96ddfdca21 | -11.03557 | -54.00317 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf0d05d4-affd-365f-82eb-19347204f088 | -10.2999 | -59.09333 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09c18640-4a95-34c8-9f07-8801e3db866a | -11.13812 | -53.92959 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 879ee28a-f076-375b-bf23-1bb6a30dc283 | -14.68563 | -52.68829 | 2025-06-01 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49da7c71-00ad-340b-bafa-f5e0a47b0e8f | -9.80355 | -54.72204 | 2025-06-01 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a39fb22-ac5e-3afe-ac77-14b44932dc11 | -14.65325 | -45.4125 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d55d3e0-d05d-3ed2-a9e9-62bb543d2a55 | -10.82552 | -56.94786 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9bc7a80-31b7-35f4-84ce-30e46b81b8c5 | -10.14351 | -52.14039 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8308670e-76fa-35cf-b469-59231263f929 | -10.98331 | -59.16115 | 2025-06-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75d11ab8-ff45-3cf2-aad6-13ae9b624152 | -14.01855 | -55.12011 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acc4ef03-9c75-354f-ad50-e4f5143f3f47 | -10.465 | -47.94595 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04210cd8-e9bf-32e5-9771-f029f06d28a8 | -12.0208 | -49.52101 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efbe9d47-baae-344c-88fd-76a08c3b840f | -13.09648 | -45.26803 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c9d2fb-962a-3e56-b705-9730834c009a | -10.67879 | -57.6086 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dfee610-ce7a-3c24-8474-06076fe7255c | -11.07597 | -54.77027 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b39542f1-40a2-3439-901e-e5d41e26bbf5 | -13.10127 | -45.27684 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7639f395-e152-3395-bbce-50ad75935107 | -11.70911 | -56.45352 | 2025-06-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a4d5418-b6a2-3947-aee3-2b496a72d8c6 | -13.10224 | -45.26873 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9632d832-3f2c-3a69-9eb1-5e15bb590cd0 | -10.61402 | -57.60995 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4b2b4f-eec6-355d-a066-a65ae848ba4b | -15.89867 | -46.01242 | 2025-06-01 04:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ba29f8b-62b8-381f-9977-6d8ec2ae47f6 | -12.01597 | -49.52452 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43f1336c-59a1-3082-8581-dccfa23e8e5c | -12.12419 | -54.59892 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69421714-edc0-3264-b1c2-578795bfd0fd | -11.14263 | -53.94512 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d793256-b44b-342e-98b4-edce951d804d | -13.09684 | -45.27077 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 226d1579-fb83-3d86-b3d8-a94bfe99ae78 | -11.57371 | -47.45988 | 2025-06-01 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 096fb83a-2aea-379c-8f75-7244ec26167f | -12.12474 | -54.59534 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c1eab1-2509-38ff-834a-42d0b2ff3d23 | -12.12141 | -54.59481 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10b0395a-a6b7-3d51-b0c9-e32e9e0b1d0f | -11.08205 | -54.77485 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f8a623-3092-36e2-8410-91f8d3143601 | -12.52243 | -57.1932 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8292903c-9ed1-3e45-8229-b4701c4cda9c | -15.56858 | -47.85642 | 2025-06-01 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f1e4b9-cb3b-3c65-857b-8d312acff4e9 | -12.72094 | -54.97464 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 90dc6b99-d7c2-379f-bf97-5d803ba0e777 | -11.14655 | -53.94203 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4586414f-50ff-34d5-8457-89e89de80163 | -12.08583 | -54.58179 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e69c0075-237e-366d-b11c-5a0f108718b4 | -13.10215 | -45.27552 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b59a945-c0f2-3a81-af98-976acc67ab9b | -11.69964 | -54.55759 | 2025-06-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 664faf2b-d85a-32df-8d6f-9d0254e08781 | -12.02507 | -49.52159 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a21b63f7-c809-3ba3-96cb-362a88a9b454 | -14.60509 | -47.96766 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1de915c0-225b-3585-836e-c6c23b33d332 | -12.72204 | -54.96753 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f1d6ac-ea54-34ed-b1d0-932542829b6c | -14.69929 | -45.11079 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27921689-6b76-3df4-8a82-f5a28b0d95ed | -14.68626 | -52.6839 | 2025-06-01 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98258fee-336f-3bb1-8583-4266637d2293 | -12.02991 | -49.5181 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b17e23be-e168-39c0-a1fe-b36050ad0fd2 | -10.21536 | -59.33555 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc491bcc-76e3-32a6-9cd5-9acade864a36 | -10.14707 | -52.14095 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 301e571d-7f80-36f7-ac2d-4877e6018b81 | -15.07814 | -48.94579 | 2025-06-01 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 719ad189-ec55-39c2-945a-672e916d3c55 | -13.63546 | -52.18045 | 2025-06-01 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a8d045e-df8d-3320-a6ea-1ebe5afc973f | -11.57452 | -47.45395 | 2025-06-01 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e1a762b8-d6cd-3f64-ba06-ca4e7661584f | -14.60789 | -47.96801 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8650df36-85a0-39b1-bc65-045bec8bf1bf | -14.02631 | -55.1361 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8cc57a-6c94-358f-9409-adcd9b0918b1 | -12.90406 | -55.04057 | 2025-06-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4b921c-8fc9-3957-bec1-9b81d2251d50 | -11.91902 | -55.43553 | 2025-06-01 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b28fa54-55cc-3f44-8eea-7b850c847231 | -10.46102 | -47.9403 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fd373b8-abda-30b1-bd1f-d281b00268d1 | -10.0776 | -52.75305 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98cb9186-47fc-34e7-93f8-eec61096d798 | -11.45264 | -55.01052 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 030a330a-29ba-3253-a3f1-a123754cad77 | -11.83393 | -51.27401 | 2025-06-01 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a0266f-b4d1-3d94-b018-992d9c7a1081 | -12.52825 | -57.17899 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29b9da27-826a-3b88-8212-be3139c714f1 | -10.46897 | -47.95156 | 2025-06-01 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 59d17e45-65d6-3474-bc8c-ca6a05877e01 | -14.01744 | -55.1273 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| edfdcfdb-2974-360e-a812-e1719522b64f | -14.69878 | -45.1153 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239d4145-e656-36d7-a086-9d930681c041 | -11.4233 | -55.08895 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
