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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9bafd43-9283-338f-8898-86b1a07fde6f | -14.34132 | -58.94773 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc2b5f10-5eb4-35b7-be99-b24789b0a45b | -14.33791 | -58.94721 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1fc1fa3-f04f-3e7e-8747-53e3033f3da0 | -14.29554 | -58.99852 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2569405d-ae4b-3d77-8b48-a688e0fdd12f | -14.34077 | -58.95149 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaf10750-9cd2-3f71-bccc-3aa1fef4f49c | -12.36337 | -63.4439 | 2026-07-29 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8f28cb26-65c5-3572-8067-7662d9350713 | -14.3226 | -58.95651 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 023cfe5f-51b2-3705-8af6-91e347952392 | -14.34814 | -58.94878 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c102a3b4-49af-3966-96c6-a09d8122af79 | -13.56575 | -49.04956 | 2026-07-29 05:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e76a6c-c1a3-324b-81d4-4f2fb5401bf5 | -14.3029 | -58.99579 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77ddd686-024f-3d5b-be63-12660535276a | -14.19074 | -51.90218 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5130c99e-9494-39d6-a8b3-d5efa54c8d55 | -13.73353 | -51.91411 | 2026-07-29 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 21fd729b-aecd-3a0e-bcb1-e097b6c2decb | -11.73662 | -57.80899 | 2026-07-29 05:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b5fca1-f613-3bc4-8488-f482be96c403 | -14.02012 | -53.96926 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aa6df63-4a16-31b3-a8df-09b42e0ef2c1 | -14.05325 | -53.96 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82c61e7f-7bfa-32c0-adb1-986d338dbfef | -14.00531 | -53.95948 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58002a12-c1bf-3611-90c9-781da89b079e | -14.05775 | -53.96055 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a35d2840-b880-38cd-ba2f-b658248f225d | -14.0092 | -53.96466 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c693311-15bc-39fb-bf2e-d5ca940846e6 | -14.21775 | -59.0019 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 331e2d8f-1e7b-38ea-9562-6c7b2ed08566 | -14.033 | -53.9758 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c32836-d16a-3f7c-8d25-43aaf8c3c01b | -14.19 | -51.9085 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b76700e3-70e8-371b-af17-90966fd934cd | -15.40211 | -55.93449 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6eaa1f2d-4e46-3670-84da-4b4248d2ab5a | -12.35909 | -63.44746 | 2026-07-29 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d2d83c9-1dd2-32a8-bacb-7c92c08d2603 | -12.36268 | -63.44809 | 2026-07-29 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7580e8d9-43bf-3d2f-a1b7-235b79648dd9 | -14.00723 | -53.96271 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151b120e-1a0b-3fa1-b72a-00840fa74f15 | -14.19554 | -51.90605 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35011af1-3a11-3c2d-984a-4d846030d416 | -14.29949 | -58.99528 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5612a93e-6e6b-354a-a133-cb963a1e84f6 | -14.06888 | -53.98089 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fc5fbc6-8ed5-32e3-849f-738b323d050c | -14.30235 | -58.99956 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827fc1b1-8d63-3a47-a62c-6bc971b3612d | -14.31808 | -58.96354 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bac5459-2858-3243-80a7-5da8e7971edc | -14.33054 | -58.94994 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd7709ce-8c7b-3b9f-85a8-693ea43980eb | -12.37054 | -63.44514 | 2026-07-29 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f69c82c-ac80-35c1-8879-7f9c4f8becfd | -14.09038 | -53.95564 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e7aa04-45df-3d1b-b090-1c501170ac7c | -14.06948 | -53.97618 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77d70d28-1c64-3ad6-8f65-c201f37ccbca | -13.57243 | -49.04561 | 2026-07-29 05:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1e0f0e5-16f1-36d5-81cf-258cc8a57e35 | -14.0151 | -53.93594 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1058d6f1-efa7-31ec-b09d-db9ba92a2359 | -14.30575 | -59.00008 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6c14fd4-f3fb-3089-935e-db183caef50a | -14.19037 | -51.90535 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4160c1c9-9363-39e7-9ba2-6920bc83a07e | -14.31863 | -58.95978 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d930703-2fc8-34ff-855e-c2a705c86653 | -13.7284 | -51.91339 | 2026-07-29 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a84ea1aa-9c6f-3666-8961-42b6699d3ae8 | -14.0246 | -53.96993 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9664fc7-e484-3fa4-aa9c-1042069afbf7 | -18.8028 | -53.14449 | 2026-07-29 05:21:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b0a1d38-9a9a-3e14-908e-179fea9124a6 | -14.01116 | -53.96791 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0691cd65-ef53-350e-a104-00bfb810236d | -15.41462 | -55.93279 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63f80ea1-8cf4-3de4-bbf0-441e04758957 | -14.33395 | -58.95045 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac2eb6b0-50c7-3e63-8fbf-2e6c949e8f9f | -13.99364 | -53.94378 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b88ea761-bfc8-31bf-b5c0-57f846118998 | -14.06225 | -53.96111 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f7133f6-170c-3a20-95e4-e7a77321ac55 | -14.06438 | -53.98038 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45793cbc-9ef8-3f0d-ab12-2e278839a089 | -11.64204 | -60.45086 | 2026-07-29 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c2e9f2a-6267-38d6-b4bb-ffd23808a92b | -13.98857 | -53.94757 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd3d621-5063-37a6-86b6-1462159f7997 | -14.03748 | -53.97647 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84514b47-9ea2-32c5-a9a3-ec2595db7c7e | -12.37123 | -63.44096 | 2026-07-29 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0731458-1e27-32df-9ce2-e23427d8e682 | -14.32712 | -58.94944 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c364cae3-47e2-305d-8361-4c67513d6ee8 | -14.03995 | -54.10113 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b5d99f8-ca46-300f-b46f-e01d6783f262 | -15.40567 | -55.93856 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9071c99f-f785-3be1-a3e9-33734552bbf0 | -13.73067 | -51.91583 | 2026-07-29 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5d56b328-43b7-30f9-9b6d-e476e0ed2e28 | -14.29139 | -58.99805 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f8e7dd7-cbc7-32d2-a720-b89d7c960818 | -14.05716 | -53.96526 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a3dd59-d198-3668-8a6f-3ffdc0a7cc2c | -14.19517 | -51.90921 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4eca033-984b-3f24-9f4d-8571779c96c1 | -14.01816 | -53.966 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a191e2e6-65d3-31a5-9f31-78dab0d22c9c | -11.4284 | -61.42906 | 2026-07-29 05:21:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec1ce1b1-eb0b-3b39-b63c-d10d7f27bea7 | -14.18963 | -51.91166 | 2026-07-29 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8ee1078-cd3f-350b-9c75-feb5e36b43c7 | -15.40479 | -55.91403 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ef70fe4-f3df-300b-9575-65dc0ff17430 | -18.79822 | -51.24636 | 2026-07-29 05:21:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3d0752a-a26c-3860-9ec7-374629a11ae6 | -15.40433 | -55.91753 | 2026-07-29 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add46b08-f8d1-3f91-aafe-1830418ae6a2 | -13.56626 | -49.04478 | 2026-07-29 05:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c66eee20-d8fe-32de-b09a-4723a14293a0 | -14.34417 | -58.95202 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 997c41f7-9dfa-3a23-9ec2-e9872287757a | -14.3345 | -58.94669 | 2026-07-29 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ba08adb-d870-367b-81d7-2cd0a845faad | -14.0162 | -53.96406 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99345218-e823-36e9-b72c-49abd15b1958 | -14.02205 | -53.97118 | 2026-07-29 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 317c6088-05bf-3b09-a13f-ecf884157ae5 | -20.62202 | -57.28438 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fa2f6d7-be82-332b-a093-17edd8223789 | -20.60048 | -57.24147 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e10fe518-04ce-390b-bf10-fd50ecff873a | -20.59564 | -57.23616 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 635268f3-14ca-3b45-b97c-211e55259109 | -20.60091 | -57.25915 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab99818a-076e-3582-9d03-31c89466e291 | -20.60375 | -57.24746 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d12fd76-a239-3807-9c46-cbb7d7dc199d | -23.84002 | -52.86321 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 142dfe9b-8af3-3997-a1d8-a0502f5c5dea | -20.59721 | -57.23545 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98f9cbd7-7042-3541-8193-bc45d54c9866 | -23.09742 | -52.68392 | 2026-07-29 05:23:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a15abe23-3471-3064-abd0-b6b2a5b25ae3 | -23.84586 | -52.85962 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c4636e3-6f15-318b-bb15-46d786791fda | -20.62596 | -57.28514 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ecbb35c-e2e6-3319-93f5-7134e5d627c3 | -20.60233 | -57.2584 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3287f9aa-488d-3c16-a189-4498edae253a | -20.60304 | -57.25292 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1278d8fd-8402-3ad8-a452-ab35a874a547 | -20.9089 | -57.47754 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 3666b2e7-872d-3792-afdd-7b77a51051c8 | -20.60158 | -57.2537 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f912777-ad77-3e72-acbb-3f7f28bb576b | -20.9043 | -57.4823 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f21bd07f-4ac8-3592-8ac6-44b2bbcba33d | -20.60488 | -57.25973 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6363a463-447b-3429-9395-da33cb9e8f7f | -20.60293 | -57.24274 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a814e63-0bfb-32f0-8f5b-fba640bbcaf4 | -23.02765 | -52.65693 | 2026-07-29 05:23:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f37fe49a-3184-34b3-bdd5-6aa3aaa0a863 | -20.59696 | -57.26857 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab24b3b5-266b-3266-aaa3-b3f38a78e6f4 | -23.83378 | -52.86154 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 88a19f7c-2cd9-3690-998c-097c3f9ff3ea | -20.83848 | -57.83605 | 2026-07-29 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8aa8d581-9b68-327a-8408-4e139abac119 | -23.83341 | -52.86556 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7c9a6ba0-3e61-369e-8493-2b3d1586c354 | -23.83891 | -52.86596 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c05a2c44-228e-3af5-8bf7-462c0ee904d1 | -22.37939 | -55.7416 | 2026-07-29 05:23:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9ce0383-3671-3845-82fb-972abd507aea | -24.49063 | -50.12423 | 2026-07-29 05:23:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e9a9033-a21c-3185-9d07-65c538f6fa46 | -20.90497 | -57.47696 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4f7bc71d-da03-3809-a43e-817767f60ba4 | -20.78005 | -57.86343 | 2026-07-29 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e83c2210-b6bb-3953-9a80-0c9f2f54750c | -20.79411 | -57.8758 | 2026-07-29 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a679d59-c434-33f0-b0bb-9b2a90533d15 | -23.83927 | -52.862 | 2026-07-29 05:23:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 114d7616-3b24-3749-ba16-82f786bcdcd2 | -20.60623 | -57.24874 | 2026-07-29 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d87bf392-7604-3bbb-ae66-f0894540cc8a | -20.79795 | -57.87637 | 2026-07-29 05:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
