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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa165097-a4f0-3692-8b65-98882974f4c7 | -12.77999 | -62.79089 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 787e09a7-b100-3dd6-b138-8bace0975b47 | -12.77941 | -62.83936 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84716af8-d706-3aa5-8e3f-ce5405d31073 | -12.77918 | -62.79559 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44638dc0-0ad7-355f-b3ea-6d8417c85010 | -12.77895 | -62.75203 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 73251725-2183-30f7-a9a6-680ee8c439b0 | -12.77807 | -62.82451 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 117919ef-a76e-3a3a-b096-e373ae4739d9 | -12.77644 | -62.83395 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c3dfb7-f383-386a-ba5e-c05c66e99fab | -12.77562 | -62.83868 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 961b9192-9ba9-3f75-bd0a-7d8d8022e594 | -12.7754 | -62.7949 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3960bdc-f4f3-3384-8fb8-c1f0fbaf6dd8 | -12.77488 | -62.77544 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28503834-13dd-3fb3-b50c-1456aa247a1b | -12.77459 | -62.7996 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4637bcad-2839-31ec-a7d5-e95898055078 | -12.77377 | -62.8043 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efeafbb4-21c9-3449-9038-a2706cd17133 | -12.77265 | -62.83326 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1723d36-d346-30c5-aad9-e371e1866564 | -12.77183 | -62.83799 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13477e4e-96e2-336a-89d4-538b3a52de9b | -12.76836 | -62.81303 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| addbd823-3491-352e-85a1-f7c9fb80b23d | -12.76805 | -62.8373 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70fd75b0-6a58-38e9-89cd-182654daa77e | -12.76754 | -62.81774 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50979ac4-1494-3e30-a0ff-4b7a2902eeb2 | -12.76723 | -62.84203 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6ff4035-3e79-3347-baef-c1845477d62d | -12.76703 | -62.79823 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 57a29301-aae3-312c-a023-06b9d36d8b83 | -12.76672 | -62.82245 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea798f3-f110-325a-ae6a-8a235760b123 | -12.7654 | -62.80764 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| de0365a5-3852-3197-a57e-6e839e091e48 | -12.76476 | -62.85622 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f9a47a-ea6a-39db-af52-cd578bf27df8 | -12.76344 | -62.84134 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54182ba4-bd0e-3315-b819-580885a4c7dd | -12.7618 | -62.85081 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7bb40b23-c6a3-3a3f-b08c-65348888f504 | -12.65898 | -63.11339 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71c5261c-c42f-369e-b1f8-92d1a57ab408 | -12.99778 | -62.70089 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1b82da28-c08c-3a8a-9651-145ac13d2d6e | -12.99403 | -62.70021 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4875de7d-43ac-38f8-9b11-d893c5739183 | -12.99323 | -62.70482 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b5d54c4c-5a8c-38d8-b00e-eb6e0ce748cf | -12.99243 | -62.70943 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 641a3296-e8bf-3103-8025-7e400c343f51 | -12.99029 | -62.69952 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a4396404-7102-35fd-9442-718bf88c521c | -12.98949 | -62.70414 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7e91d903-019c-3242-8d08-992f2210bcba | -12.86588 | -62.72253 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 630a5562-0b0b-309c-9f97-a0172569a7da | -12.85902 | -62.73768 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f94ac5-7fa3-3551-bd3e-c3e853367c2a | -12.85886 | -62.74045 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e73b1fc-eeb1-3415-8bd1-65e4508cb459 | -12.85823 | -62.74234 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1938b01e-594f-34d5-9f83-7604124a6570 | -12.85818 | -62.67816 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36860dce-2eb9-319b-bc64-10d38c847c33 | -12.85559 | -62.75909 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5880f2b6-55f2-346e-b561-6720f649a040 | -12.85428 | -62.74443 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a469309e-2d01-38ab-a538-dbc00268f75e | -12.85216 | -62.73444 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f52524e-3cb6-3bef-8458-456544498f7a | -12.84774 | -62.73563 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa9b4da-0190-3f76-810e-91460b21ffa9 | -12.84758 | -62.73841 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6e46541-af85-37f2-b08d-07590f951403 | -12.84635 | -62.72097 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f6977c3-b893-3b28-a77b-33929b4da644 | -12.82835 | -62.71292 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a039125-5c08-37d1-942f-c2408628252e | -12.8245 | -62.80379 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 199ac45a-c899-32d1-af4a-7f0525933098 | -12.79234 | -62.63013 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85fa4c45-fc02-3e44-ba54-60eef9081064 | -12.79213 | -62.78824 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5543063c-92f7-3587-9d8e-1d4d3b06eb44 | -12.78998 | -62.77818 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92b30a7d-8464-34c9-9413-e654e570dd8a | -12.78944 | -62.75876 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f82143-da14-316d-b9b6-0ae008f98699 | -12.78917 | -62.78286 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e939991d-2412-3af2-a146-4feeb6b57ced | -12.78782 | -62.76812 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8178f76-2092-306e-8fb8-200fc362bb19 | -12.7862 | -62.77749 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c2aa2f0-a2ef-3d41-a098-ef870412a32a | -12.78567 | -62.75808 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62bc934c-7a4b-3eb0-81eb-7fd3aad09666 | -12.78539 | -62.78218 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 316ab51a-82b9-3dee-b18d-82d354c7f2d5 | -12.78486 | -62.76276 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6601542b-8ea7-3daa-968f-63015d467ecc | -12.78405 | -62.76744 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38fb45fe-3c44-3096-b8dd-614dbb132eb4 | -12.78192 | -62.62351 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 458dfa61-76e5-3b0e-8e20-498ec8ef45d4 | -12.78109 | -62.76208 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc41238e-2e5e-36c6-a21c-e9dc1be4a45b | -12.78028 | -62.76676 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2028193-3ee6-3438-985c-64c1fc45ea66 | -12.78022 | -62.83463 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9ed643-37f8-3c6c-921c-63ce46616a02 | -12.77976 | -62.74736 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2fd93800-b935-3c8b-a99f-b6c7794a1189 | -12.77951 | -62.70409 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26e1e9c-5b69-30de-9c62-587880243213 | -12.77947 | -62.77145 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f08cf63e-f223-373a-94c2-855c7c02a788 | -12.77866 | -62.77613 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 171c99e9-9d9b-3af4-8026-83b99c58e06b | -12.77818 | -62.62284 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a1c8f579-841c-341f-a9f3-64a004eba7b5 | -12.77726 | -62.82922 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c356237-c6af-3a33-8136-dde3fa9a22e2 | -12.7757 | -62.77076 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16ad3f16-1984-323a-b33e-5be0b68d8aab | -12.77444 | -62.62217 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b1570aca-6d50-366e-9086-72bacb616d00 | -12.77347 | -62.82854 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dee6647-8224-364a-b5a3-f1144d558c96 | -12.77102 | -62.84271 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea6738b8-ea73-3a7e-827d-438ba9dc08f8 | -12.77081 | -62.79892 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f0747547-a61b-3ce6-a22d-42c2d489598b | -12.7707 | -62.62148 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 5144ac6e-2cd3-3398-b44d-b29e975e1253 | -12.77039 | -62.61905 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5261bc6d-3e8c-39fb-b8b6-98bb58516b6c | -12.76999 | -62.80362 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e58bec35-6151-3f64-8bfc-de4ec439671d | -12.7699 | -62.62607 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ed239e7f-eeb7-3e8a-8330-4f200e57f8e1 | -12.76961 | -62.62365 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| dfc97e96-cea5-3c94-8b82-cc46cba1169b | -12.76938 | -62.85217 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408cbfdf-8b18-3986-a914-15fd4506d9a1 | -12.76918 | -62.80832 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 2e0d213f-ba26-3e6f-b51e-dc394357cd4e | -12.76884 | -62.62825 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 9ea67cf5-bbf4-3532-a4b7-f12fad1b77d7 | -12.76697 | -62.62078 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 482a9e42-b45c-3309-a01e-4b0f885069cd | -12.76641 | -62.84676 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54d64f1e-b804-3a85-9227-fe8c9cbfa6db | -12.76622 | -62.80293 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 670e5537-6242-3c56-ab2e-753fb07601df | -12.76617 | -62.62536 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f9b5af58-bb07-3325-8f04-c6ee1f61784d | -12.76587 | -62.62294 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| e391aac6-d9aa-3994-b3ce-57b6bffa9e0c | -12.76558 | -62.85149 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d8e6d06-f651-3082-b89e-37c86a769247 | -12.76536 | -62.62996 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e43f2f77-75ca-3d2a-8381-b05880dc8303 | -12.7651 | -62.62754 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 5f7c3a59-57b3-329e-b1ee-beb4338226d2 | -12.76458 | -62.81235 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efd37f50-7bd9-3376-a541-d868c1234829 | -12.76376 | -62.81705 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bdb385f-5050-3b9b-b134-693bfecbbf7d | -12.76262 | -62.84607 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 939f7dfa-27c4-37be-9a76-f15122d38d37 | -12.76097 | -62.85554 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f9c2cd9-1781-378b-b273-22b0d8c6a5e6 | -9.35154 | -63.80025 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b3fc17c-533f-3cd6-8d11-fa2ced4f4555 | -9.35088 | -63.80405 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14e28697-9be4-3a7d-9481-93b3d1342ca2 | -9.34663 | -63.80332 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fe15051-f752-3811-96c5-923faafa1e0b | -9.42021 | -63.42853 | 2024-09-28 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19feebb2-ed7d-3ef6-b31d-c5433d94e91d | -9.41608 | -63.4278 | 2024-09-28 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0eef4dd-66f6-32cd-b60e-ef75a56f8f30 | -9.41542 | -63.43158 | 2024-09-28 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1709e956-53b2-3b73-8887-0c4175c200aa | -11.66399 | -63.99867 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0073a64-dd3c-37a9-a24b-e02742a40e3a | -11.66042 | -63.99474 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f379f05-539e-3245-9b19-d6a4472f5402 | -11.65978 | -63.99831 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e00cca2-6f72-3b69-accc-31a3a7a4e06f | -11.65488 | -63.99131 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d38ed9da-db32-3a66-88bf-77b1e02d6700 | -11.65351 | -64.00938 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README92.md)
