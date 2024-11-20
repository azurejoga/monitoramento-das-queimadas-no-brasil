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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d5d0e7-6ed5-3e54-8a89-7d99ab492fdf | -1.20218 | -51.77148 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0242fec-9a43-3b79-9b39-ba53e59b5b1c | -0.1108 | -51.43992 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e69feb2a-1aae-3c69-9861-a47c9afd0843 | -1.09506 | -51.73604 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3238cd71-b80f-3654-aff2-929ee6177af9 | -3.19369 | -54.32298 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d50e9e1a-8294-3aa2-8714-62654c7c1c01 | -3.1389 | -49.1265 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aae829f-c092-36ff-ac85-27fbe83a4f51 | -3.79955 | -52.22066 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ca2b8ad-23ee-3103-9607-654a6295d856 | -1.33591 | -52.2405 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c97217c-bcd8-3436-915b-9711825be71e | -0.96597 | -51.72984 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc25290d-b625-360a-b579-f7e08a9b111d | -4.44156 | -46.58414 | 2024-11-20 05:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 90023a32-998c-371f-850c-ef28ef4d33f9 | -1.10904 | -51.75893 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdbf5597-349d-3a3c-a73d-93dfc660111b | -1.30615 | -52.26698 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 954d9f4a-8672-3d32-961e-3f445f29bf61 | 0.05051 | -49.53283 | 2024-11-20 05:14:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e52fdf2-fc3b-34d1-adb8-67900acc4b91 | -2.34398 | -54.75009 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6042b10e-4305-3ee2-8a25-d728797f2d73 | -2.74843 | -54.01841 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63f8554a-5172-307b-8096-fcefe8c5a7ae | -1.42169 | -46.79985 | 2024-11-20 05:14:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a62ba0-4673-304b-bf3e-94dbe3a7ac9c | -11.33545 | -55.05325 | 2024-11-20 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 700718ac-ce33-3b6f-ab27-6d5cb885ebd9 | -11.49184 | -54.2855 | 2024-11-20 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7548cb49-b4e4-350c-b305-eb376aff0104 | -9.9942 | -55.65246 | 2024-11-20 05:16:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02ba5b8b-851a-3e75-8948-75c92311a7f7 | -11.1008 | -54.62126 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e62abb-826b-39db-a2dc-4ef1df22bddf | -11.09462 | -54.63557 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 581cc31a-9538-3be9-8a34-92f8d552eefe | -11.11104 | -54.63797 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f55f2a3d-1faf-3116-9fa6-4b3d9f8cda23 | -11.09155 | -54.62751 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18ec2924-2683-3840-9e6d-d93d0dbdc62a | -9.40824 | -54.79909 | 2024-11-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 363161c7-15dd-3d31-b1ff-4dc94eae0e0d | -11.11156 | -54.63425 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6772d7d-b54a-32a0-938f-54580312b267 | -11.10282 | -54.63683 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddd3abb4-e579-3c6e-bbda-661d53e6c52c | -10.11856 | -54.20714 | 2024-11-20 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d66f9b24-40a1-358d-b93e-22d245fa053a | -12.58158 | -52.49266 | 2024-11-20 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ad635e3-3b15-3aa9-b20c-dae8bba71959 | -11.09976 | -54.62876 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2766dbfd-98c6-3cd4-90a1-770e735556dd | -11.10334 | -54.6331 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 030070ee-2117-3b65-8c7e-397575652bcd | -11.10386 | -54.62937 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4dd3e698-c979-3643-957f-fceb08b3584e | -11.49663 | -54.28206 | 2024-11-20 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f04ce8d5-5373-3b0a-b11d-6140b10f5643 | -11.0941 | -54.63929 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c585d0-aad5-3a3b-afa5-6046aa7e08c6 | -12.03638 | -54.65543 | 2024-11-20 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e80282cb-0205-3020-8fc7-b48363a2fa8b | -11.50086 | -54.28262 | 2024-11-20 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4664a62f-6abf-3b0b-b76c-30a9bd867b60 | -7.21127 | -55.00148 | 2024-11-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77177d00-4c95-319c-8873-2cbd4a84a4f7 | -11.10849 | -54.62622 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 284f2182-4666-309a-8dcc-bab53311cee1 | -12.0369 | -54.65158 | 2024-11-20 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb3a8c6d-de96-3824-b1be-d897165051af | -11.10797 | -54.62996 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 987f05cc-a61c-37f8-838b-21f5664894fa | -11.49239 | -54.28152 | 2024-11-20 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 388f7942-de33-323d-bc83-1cdf7d18d03e | -7.21025 | -55.00365 | 2024-11-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5662d04-eb14-3c74-97ac-092cf9b629ea | -11.09514 | -54.63186 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97286099-26a2-3e45-b6aa-512380ddaf18 | -11.09872 | -54.6362 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5691f653-7cb5-305b-b5d4-ab1ca5d12d08 | -11.11208 | -54.63054 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 26d9e33f-bb1a-3d97-b78c-f97bfc6e6776 | -11.10745 | -54.63369 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb31bfe9-c309-3496-84d4-3e672e8241bc | -11.09206 | -54.62377 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6901be2-9836-32ae-9279-84489f4b8fa6 | -12.12446 | -54.28986 | 2024-11-20 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0504edb9-1d3a-3807-90cb-d1afcc1fecb1 | -8.63379 | -68.09739 | 2024-11-20 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 32574219-6fb5-36a3-9728-3541fa1a78fa | -12.03742 | -54.64774 | 2024-11-20 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f30d8bbf-6e2a-377d-9017-8229667aac01 | -10.11495 | -54.20259 | 2024-11-20 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f74d886a-6425-3ad3-ab0c-4e06938e1a4e | -11.09617 | -54.62438 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 06ed6623-eb5a-3008-9a1c-a018a8fa874b | -12.1202 | -54.28923 | 2024-11-20 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1aff9a3-dc1a-3d00-805e-b1bf951bb52c | -11.09258 | -54.62002 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881aae26-ffbc-3bb2-a2e8-b0c224f7513b | -11.37743 | -54.92811 | 2024-11-20 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a145b8a7-944e-3807-8de4-3a2ddee1d3cf | -11.10028 | -54.62501 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5aa02986-97c8-31bc-ab14-272840d46b76 | -11.10438 | -54.62563 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f18b5981-3a63-31bb-9e64-0820d70c2556 | -11.09565 | -54.62813 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d7de698a-8d14-30b7-98a0-b99d122072ba | -11.0982 | -54.63992 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ae71bf-c3ba-36ca-a743-fbf8f6915930 | -7.21093 | -54.99894 | 2024-11-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f792126-df42-385b-a1d8-1b4dce544870 | -12.79142 | -57.02253 | 2024-11-20 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 096c3b82-fc22-346f-8a25-4fbcc83ddaee | -11.38146 | -54.92874 | 2024-11-20 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8af11c0-a9f2-31bb-a9c8-008c8d74bfda | -11.09924 | -54.63248 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14009f2e-177f-37c5-83ba-2b416b21d8f5 | -11.09669 | -54.62063 | 2024-11-20 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 021ef47e-cb20-3563-9a6a-dfdcf98e2f18 | -7.20781 | -54.99365 | 2024-11-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21e8d76f-7875-341c-ad11-af6ffda1efb6 | -20.30076 | -55.06743 | 2024-11-20 05:18:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d56012c6-836f-32a9-8c64-be59f304b6cd | -16.89382 | -57.51525 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6b870722-8b3f-3246-825d-c44a4b69bd47 | -15.29493 | -56.5354 | 2024-11-20 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b01ba45-1010-3e7d-a115-0bc83a2f2c60 | -17.12753 | -57.49824 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c78bb26-d30d-35a0-9bea-23ea5a720f56 | -16.44141 | -52.56302 | 2024-11-20 05:18:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a4352f3-53e9-3382-89d7-82c3017dc914 | -17.12095 | -57.49989 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f71c9f10-9311-3020-8864-8d7d8f696bca | -16.45285 | -55.9833 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 23823cd4-172d-3208-8bd4-8fb1eb15270b | -15.87411 | -53.27851 | 2024-11-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94ee999a-eafe-3243-a148-52cc8725777e | -20.20949 | -56.6297 | 2024-11-20 05:18:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4e7b451e-99aa-3d8a-a774-e3162df165a3 | -17.13216 | -57.50156 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3b435bd9-af0c-3209-a5d5-be03f9f24adb | -15.86992 | -53.27268 | 2024-11-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43eda84d-594f-3015-82b2-472c84b4f1b1 | -15.87889 | -53.27945 | 2024-11-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3145dc2-eab9-3a7f-95a7-8e364db7f27b | -20.20539 | -56.62913 | 2024-11-20 05:18:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0fdff01f-d94c-32c3-a18e-dff7e1a42552 | -17.55658 | -57.46535 | 2024-11-20 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2e6b9a82-cf03-3b7a-a299-6eba12a5ddf7 | -16.43663 | -55.981 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f6103438-9867-38a9-a1db-8d5d7f5cd26a | -16.44879 | -55.98273 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 72220f1e-c33a-318a-967d-96ba9f6b0130 | -17.13468 | -57.4829 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 41a2ec0d-1920-3f32-9087-448985f99d6f | -17.13127 | -57.49879 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 87f39688-40e4-3ae9-92b9-1995cf6e871b | -16.43761 | -55.97363 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| be42d7fb-71f4-36dd-b4f1-6cc540665ffa | -15.29879 | -56.53598 | 2024-11-20 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c35e7d8-cd33-352b-9028-426ea9d24a4b | -17.13964 | -57.50267 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 94d35bc0-7d2d-3179-98d5-e9cc91f53661 | -17.13653 | -57.49746 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 81aa8ccb-f180-3f73-b932-943b4da2ebab | -16.44105 | -52.56606 | 2024-11-20 05:18:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2259407-3e6f-3628-bde2-342db2bb0a6d | -17.6572 | -56.46093 | 2024-11-20 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 795984eb-84a7-3238-80ef-8c2db39e4726 | -17.13716 | -57.49279 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31f2e37b-388b-352a-926a-0aff48a49fe2 | -15.87052 | -53.26758 | 2024-11-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4e925ec-5c95-3e22-b2a7-b069f3662b43 | -17.1359 | -57.50212 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4a08d90b-6126-3172-85e7-80075c1c3118 | -17.60974 | -57.38823 | 2024-11-20 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a3286a9e-f00f-3b6d-8a1d-e26d35b95686 | -17.12469 | -57.50045 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2d4c3085-4561-3d3e-b331-56cd24256b06 | -17.12314 | -57.50235 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8974d6f4-c552-3448-bc0e-bfaa1ad9e5bc | -17.13842 | -57.48345 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e373d83b-348c-3425-b8de-f23b33a853fb | -17.12842 | -57.501 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 857eef09-85ac-31a0-88e7-4c07a6408329 | -16.43712 | -55.97732 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 63e067e6-8bbf-304c-afc6-74831b576168 | -16.89009 | -57.5147 | 2024-11-20 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 05881a37-5fb4-3da5-b9cc-7af9f5b1904a | -15.30333 | -56.53163 | 2024-11-20 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 511b2985-f8a7-3598-8cfd-fc9f8eebb785 | -15.87471 | -53.27346 | 2024-11-20 05:18:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72d31895-ef8d-36aa-b92c-8e09f43b4404 | -16.44068 | -55.98158 | 2024-11-20 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README74.md)
