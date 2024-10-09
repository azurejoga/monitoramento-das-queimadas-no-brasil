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

## Dados Diários - Página 220

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a05dbf8b-1463-3bbc-9d53-1ffb4134f0f9 | -4.1152 | -59.88257 | 2024-10-09 06:12:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a21f2ef7-dea2-37c6-8a75-5670e4ac49cd | -11.38264 | -58.99852 | 2024-10-09 06:12:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| babcac34-5ede-3fbd-8cc8-c9c1c960f2c8 | -11.35696 | -58.98517 | 2024-10-09 06:12:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 566cc425-cf88-3297-84ee-b28585d428ef | -11.28671 | -60.38889 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ef455bfd-2e9b-3d2e-91fd-bb52fcc10899 | -11.28536 | -60.39787 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 7992ea41-cb41-3c0b-bfe8-15e913abf1e4 | -11.27921 | -60.37858 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a2d00e6-d429-3996-93e7-bcb2c8f324e3 | -11.27786 | -60.38757 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 661d49ad-0de9-3214-8af0-c30c997b404c | -11.27651 | -60.39654 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 07520f7e-3dbd-31f1-9fc1-5d46c065f0a2 | -11.27186 | -60.48764 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 42258ff8-2a37-3cbe-8af7-40adbd00b888 | -11.2717 | -60.36825 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e22c06f-8faa-399b-89d4-8311ed7b9451 | -11.2705 | -60.49662 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0817924e-235c-3a4d-8abc-f2e805794a56 | -11.27035 | -60.37723 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0dff208a-79bc-33d9-9529-a00a912253f9 | -11.26989 | -60.56094 | 2024-10-09 06:12:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6f4d7512-dc52-3c3f-b54c-159d93a9b757 | -11.26853 | -60.5699 | 2024-10-09 06:12:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 95c6671c-0247-33ef-bde5-c2b8ed4e1db6 | -11.26766 | -60.39516 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14b9ab16-580b-3086-9675-b307ab679b26 | -11.25967 | -60.56855 | 2024-10-09 06:12:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 906b56de-74bb-3fbd-8e0e-e7a432621916 | -11.19475 | -60.45087 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a08fd26-640a-3eb6-b78d-61cd95576e40 | -11.19339 | -60.45985 | 2024-10-09 06:12:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1fb5a9ff-eb7e-338a-9fa3-3a1295bc74aa | -11.17036 | -60.61278 | 2024-10-09 06:12:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ddee4b69-4fe2-3398-b8e1-91905362498a | -11.13871 | -59.09238 | 2024-10-09 06:12:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 48a19772-3d18-32f8-8094-50ad1e2d9996 | -10.97917 | -60.7812 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d9c5b94a-debc-3829-a44c-1315553dac3c | -10.97358 | -61.11668 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| de4d41d9-e12d-37b7-8548-aafd391ced9b | -10.97217 | -61.12587 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f232267b-54ca-3e88-bcf8-1bc2a6581548 | -10.94443 | -60.94612 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21902ddb-f34d-328e-82a4-9110481d5fcb | -10.87125 | -62.02551 | 2024-10-09 06:12:00 | AQUA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d8f2f2f-b282-39e7-829a-582fd5150bb9 | -10.78423 | -61.51005 | 2024-10-09 06:12:00 | AQUA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1d3ce12-72eb-304b-a39e-06d879b9609a | -10.71001 | -63.6389 | 2024-10-09 06:12:00 | AQUA_M-M | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2416d3c-9593-3eb6-871e-bcbbb20e8a3d | -10.64579 | -55.88274 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f645cb68-9795-326b-b24b-52693e0946f5 | -10.64393 | -55.8962 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| a8ed7dc8-54b5-34af-96ae-3c1ce35130ac | -10.64209 | -55.90954 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 928180ee-736f-310f-b60b-8f422a3442ad | -10.64028 | -55.92272 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f797612b-0fe3-3a23-afb0-9255796bec7f | -10.63326 | -55.89487 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f8299b29-240c-34f6-99c4-6ff5b3ab1828 | -10.63145 | -55.9081 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f48d80e5-b056-3c5c-b3ff-407e4de83b9c | -10.62962 | -55.92142 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f8c4ad27-f031-3c24-be54-e023317dea4c | -10.49235 | -62.89112 | 2024-10-09 06:12:00 | AQUA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b16b561-3737-309d-b85b-efd73f7958d7 | -10.49063 | -62.90191 | 2024-10-09 06:12:00 | AQUA_M-M | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1a3ff609-2387-35cf-bd6b-f2ac837ca261 | -10.43919 | -60.98764 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b81a1101-7ddb-30b1-9218-87be6eeab22d | -10.43778 | -60.99687 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 920202ea-9476-363d-b27c-bb71baa29819 | -10.43023 | -60.98624 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de78c304-b8e4-3d26-91ac-91751c00f8bb | -10.42883 | -60.99537 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58a8b241-e0fd-3b3c-919b-cf70bc945c49 | -10.40712 | -61.25734 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7287f722-d099-39b5-a5b0-617bd700a683 | -10.40237 | -61.22806 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7adb2360-cd18-3be2-b63a-0f8ccc4b803c | -10.40095 | -61.23734 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 90b7bc6f-bb19-3c29-8a65-a10d3fb8d232 | -10.39951 | -61.2467 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8f62f397-e94c-37ca-9b67-ce13f302c1a4 | -10.39809 | -61.25593 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0e3fb4f2-90dd-39f7-ab2e-ad25d307456d | -10.39192 | -61.23597 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0344b57f-d249-388d-827e-a7accd0c2acf | -10.39049 | -61.24526 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| acb6eb50-ccbc-3727-ae6a-67465b421720 | -10.37478 | -55.85372 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ba1e06f4-4a70-3d47-a60a-427df14b99cc | -10.37296 | -55.8669 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f3f93b38-f666-3d85-9283-775dbd669691 | -10.34643 | -57.50258 | 2024-10-09 06:12:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 60588429-0181-33e6-bff9-11aec3b50e00 | -10.24303 | -57.82169 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 933517ab-b31e-3b92-baff-13e9109572d4 | -10.21316 | -58.7944 | 2024-10-09 06:12:00 | AQUA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1de16bf5-7104-37a7-9604-1ddb0277d10b | -10.1542 | -62.1144 | 2024-10-09 06:12:00 | AQUA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66468967-fa3e-3dce-9819-1a2d30e8b2fc | -10.10647 | -64.83943 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ecca45d0-f0f2-364b-beae-3f59896590b1 | -10.10173 | -62.50923 | 2024-10-09 06:12:00 | AQUA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5ae918c0-2695-3244-93b3-60039d583692 | -10.10005 | -62.51986 | 2024-10-09 06:12:00 | AQUA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| daaef1a2-0b8d-3314-83ff-e0a2e31eb5d2 | -10.07792 | -61.11503 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 47053217-439e-38c5-bde6-319c74b91b41 | -10.0765 | -61.12434 | 2024-10-09 06:12:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f7f91c3-dd6b-3026-95c1-9ad0f55e7d2d | -18.94808 | -54.55872 | 2024-10-09 06:14:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b1bd632f-a63a-3c3b-9318-8bd45b394439 | -18.94184 | -54.56541 | 2024-10-09 06:14:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| dc564b59-3fc1-3031-a46e-76374fc3f55e | -18.9345 | -54.55769 | 2024-10-09 06:14:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 68e9e6ab-263d-3f33-bfba-59618f0c4010 | -18.61849 | -57.23311 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 7d5b0d11-eee5-3931-b6f5-32cd50ce2346 | -18.61668 | -57.24758 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| dda36f1d-e0b8-37e2-8663-0e731669dc5e | -18.61486 | -57.262 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 96a0087d-58e6-31db-b7b8-cb7e35602252 | -18.60756 | -57.23166 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 64b5883b-7012-3502-bccb-0e684308b702 | -18.60576 | -57.24613 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 7136e9e9-6d5b-3f42-8d8e-505fee0ceeef | -18.60396 | -57.26056 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 5d4c596b-f892-35ea-8260-45f31ca8a1cd | -18.13964 | -56.38347 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 2713f623-ff31-340e-878d-f4bfcec95f61 | -18.13769 | -56.39982 | 2024-10-09 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| ad5d19eb-1666-3eae-8b65-385e3f44a882 | -17.33585 | -55.00389 | 2024-10-09 06:14:00 | AQUA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 3ea64ec8-4116-311e-a549-aa5f7c866ed0 | -17.22167 | -57.32367 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| ee940f0f-f392-35ea-9f17-967a4202b6fb | -17.18979 | -57.31934 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 697f1cb5-1198-3bbe-a99a-630a19ce202d | -17.17623 | -57.42667 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.2 |
| 60ad7daf-e2a7-3b67-9ebd-e88ef28db8f7 | -17.17455 | -57.43995 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 314.4 |
| c2a76e43-4882-366e-b630-dec386f48798 | -17.17287 | -57.45321 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 6eb72ce8-55c2-3dc3-b4b2-a6e8a0a05376 | -17.16401 | -57.43851 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 259.1 |
| f8dc0c20-e714-3362-b485-d51f87aa677c | -17.15956 | -57.43092 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 896d1d18-1f0c-3289-a7fa-efd84946e076 | -17.15891 | -56.83687 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 9a7f6804-c9c0-3bbc-aaaa-1c7c5791d116 | -17.15781 | -57.44417 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| e538c1c7-0945-3d41-b768-e303bbf52c9c | -17.15606 | -57.45739 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| d3ea71fc-64eb-3370-9cbb-559733c3f017 | -17.15348 | -57.43708 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 727aac93-ae6d-3559-8617-b0689d5867ff | -17.14902 | -57.42951 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 799a2fa2-f48e-3612-9017-986b5325adfa | -17.14728 | -57.44275 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| e72fb741-2e57-3e67-bd65-60eed24ae2f2 | -17.1472 | -57.36139 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| c4dfc32b-3b9b-3d04-8633-196de616bc54 | -17.14611 | -56.85001 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 2b6e5bb0-7b3f-35fe-953d-13de34ddff35 | -17.14009 | -57.33308 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| db412928-18da-3b57-bcd8-2184cf2367d0 | -17.13849 | -57.42808 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 73da660a-9c42-3606-9dda-042df5292ace | -17.13676 | -57.44133 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 9aad4dfa-f1d8-33e7-b1b8-762091493870 | -17.13661 | -57.35995 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 21b8873c-44b1-3c7f-9baa-1419511d4469 | -17.12796 | -57.42666 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| b9c3cdc1-13f0-389a-a440-370af0b27718 | -17.12624 | -57.43991 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 0596fa5e-f435-3c8f-b0fd-ad3caafc45b2 | -17.11742 | -57.42523 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 902022fb-ddd7-3042-a733-d7b71a1ea1cd | -17.11571 | -57.43847 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| a4e9205f-42ec-3127-94c0-c0378881929a | -17.114 | -57.4517 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| afa0bea3-593b-3aea-b58e-679bff1187df | -17.10827 | -57.32878 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 40521c3b-7491-3cee-b7e0-83f578dba736 | -17.10657 | -57.34223 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b50c6594-08eb-3f66-89fa-2b709ba2898f | -17.10519 | -57.43704 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| b480bf2b-5517-34ca-9dc2-c6290917dc46 | -17.09597 | -57.34079 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 59e95e0c-3c17-336b-af2b-e25d76f27ea4 | -17.09427 | -57.35422 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 30a0e80a-0ee0-3706-ba3b-ac17af7d7702 | -17.09258 | -57.36762 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |


[Clique aqui para ver as próximas entradas](README221.md)
