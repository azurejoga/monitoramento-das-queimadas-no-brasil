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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de96ca5-b4f1-3d09-b6c5-eb0abf5bc910 | -20.04341 | -41.32446 | 2025-10-03 03:47:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a1da646-229f-3dd2-b73f-59ce323cda58 | -16.26891 | -47.09448 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e38f8f-2f83-329d-848c-be700f3ce36d | -19.87314 | -43.64875 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3607b8d6-7f02-3f3e-bd81-769f60d0ded1 | -19.89287 | -44.18697 | 2025-10-03 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c11bc59c-d1f9-384c-a653-e078d5de5390 | -19.84587 | -44.08359 | 2025-10-03 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8c8e182-dd69-3df1-801d-4cf0a7c42fc8 | -19.47203 | -43.65497 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a6711d1-c826-38f7-ad4f-50f168186c8a | -18.45326 | -43.70886 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4127d3a3-afce-3390-995f-a5f73650e1f1 | -19.36361 | -44.2548 | 2025-10-03 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9847c71-d39a-3f28-8e82-21960dc143da | -19.45586 | -43.65226 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e7ee17c-375a-3fb4-aa58-e08dffa8c942 | -17.2181 | -46.98471 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac6a3a1c-6759-3eea-b26d-635647550213 | -19.83677 | -42.29571 | 2025-10-03 03:47:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e68dae60-3276-3f12-9a6c-62e3db3b768f | -19.95173 | -41.64327 | 2025-10-03 03:47:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b0b2577c-4753-315d-a771-59f261dcda67 | -20.22129 | -41.39038 | 2025-10-03 03:47:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e5499fdd-9eda-3e56-a420-a4acdebba07c | -20.01058 | -44.18842 | 2025-10-03 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 04d10f35-2304-3465-8b6f-b26ab21598ea | -19.84733 | -44.07578 | 2025-10-03 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3a9bdab-af0c-3433-bbf2-08a0d95a5204 | -16.36048 | -47.07186 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a697b461-e042-3887-a2eb-64f5d3f8d83a | -20.00722 | -44.18363 | 2025-10-03 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6f6fb465-38a2-3a8f-950e-2628654d97df | -15.25263 | -50.12583 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8235afc4-4c6e-30ec-93f6-26c8fd2e704f | -19.95451 | -41.64854 | 2025-10-03 03:47:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 33264182-8665-337d-ae25-427b185b2c87 | -20.04264 | -41.32896 | 2025-10-03 03:47:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 486ae60e-93c6-3d55-8d32-e60d92f0ac92 | -17.63012 | -44.44761 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94925a04-3cf5-3f13-bfb9-731729566a49 | -20.36924 | -42.20332 | 2025-10-03 03:47:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e1241774-5356-3065-8bb8-d278bd96e621 | -17.62579 | -44.44658 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 909cf749-ffe1-3895-9e7e-6a252e412025 | -15.24775 | -50.11723 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 20613540-b7e8-3ebb-941c-3236227768aa | -17.99064 | -45.02962 | 2025-10-03 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a08a8894-95c1-3649-b86b-79fec38f093f | -19.72643 | -46.55571 | 2025-10-03 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd52acbb-7822-365f-9955-d3972580dc99 | -18.51431 | -44.03288 | 2025-10-03 03:47:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b61f4e8-0d7b-3f7e-a621-15f7a30ca2eb | -21.55867 | -45.27763 | 2025-10-03 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4dff17d5-2a63-3b19-92f3-0f5997c2fbca | -19.72329 | -45.8782 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 098a9b40-8eaf-37b4-b3fd-6a0cbbc6b0fc | -17.49313 | -43.4725 | 2025-10-03 03:47:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64f63ebe-5ef7-3b6b-a1c0-bc3e3013d7e8 | -18.97831 | -46.97288 | 2025-10-03 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c22a17d-5be7-3641-95fc-9cfbfd25a1f5 | -20.49322 | -43.92774 | 2025-10-03 03:47:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a980af6-a542-39ec-b177-9c2866a05e10 | -18.43467 | -43.71719 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dddeaa75-44b7-31c2-a74d-6bcc72170d32 | -16.76248 | -43.96336 | 2025-10-03 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f7d74ec-4f91-353f-a8ad-cca241726cb5 | -15.75799 | -47.7734 | 2025-10-03 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b8631cd-c26f-3379-85d4-74d07ce2e1ab | -15.24713 | -50.12166 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cbdfd9bb-3629-3376-a2a3-c552f02add37 | -19.90236 | -44.50306 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7c4b188b-7ea0-3b9c-9051-b1b0040a5ede | -16.36756 | -47.01087 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6678b8f-49d2-31ad-8f4d-51763fc74e43 | -19.72402 | -45.91711 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e220a7a-de84-31ca-b060-f3cf189c5c24 | -17.17686 | -47.02229 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23324251-a4e7-3963-9b47-a4409ea43d76 | -18.68244 | -47.83428 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31bca1ac-38b0-30a6-a092-748a8b40efcb | -19.96555 | -43.65066 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9d07a5ed-dce4-32f9-9897-57481c647295 | -19.60096 | -43.84227 | 2025-10-03 03:47:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c39219b7-9a77-3672-b234-a0754d02df8c | -19.84177 | -44.08278 | 2025-10-03 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c2bf33b-ce09-3912-a2d3-958fc509b553 | -17.91644 | -43.93632 | 2025-10-03 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 758e3b53-e627-30e2-8ab9-f21c5c75430a | -20.36267 | -42.30351 | 2025-10-03 03:47:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f118dea-fb7a-39eb-98fc-d737788e5b2a | -19.60141 | -44.63414 | 2025-10-03 03:47:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fc3adadd-546e-3871-90ef-8b750a29c8aa | -19.90204 | -44.50307 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5544a4d-8697-343f-81cc-147e3b40999f | -17.21004 | -46.992 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11db5c89-5ecd-36a5-a078-c902fecddf13 | -19.01965 | -49.75401 | 2025-10-03 03:47:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17664a1-e8f8-33e6-b25f-21369be58780 | -19.8699 | -43.64401 | 2025-10-03 03:47:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9a77369e-0454-3164-8e56-4e14cc68bd07 | -21.34409 | -45.00912 | 2025-10-03 03:47:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cdaee97e-8242-3d1f-8de8-cf99be4fa615 | -19.59089 | -45.89771 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8552961d-8f9c-35e3-8ce9-0e3b961ac057 | -19.51124 | -41.96463 | 2025-10-03 03:47:00 | NOAA-21 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f16765b4-2a6a-3e92-9a71-b35314d2ac41 | -19.94818 | -46.80922 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70da1aa1-7c32-3cda-8676-ecf0bddaaddf | -19.60223 | -44.62991 | 2025-10-03 03:47:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2452b715-a164-3d62-90bc-ca4ba5d89a32 | -18.50072 | -43.56828 | 2025-10-03 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c875c6fe-780d-395d-aab9-53d6a9f31fe1 | -18.51354 | -44.03692 | 2025-10-03 03:47:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58ea16dd-caf7-34ba-a2d4-22b3accf2067 | -21.58841 | -45.28493 | 2025-10-03 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7b38d220-cc5f-35df-9f23-b9feaedc1909 | -19.16748 | -46.68787 | 2025-10-03 03:47:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43ef60d8-c0fe-3a96-9b80-1d463ccb86d8 | -20.13273 | -44.0099 | 2025-10-03 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a821d2f5-49b7-3f3b-84c0-6a3e77faf2ef | -19.73124 | -46.55666 | 2025-10-03 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29bbd06e-b3bc-3a6e-9d41-94fc89fa5bc1 | -19.84252 | -44.0788 | 2025-10-03 03:47:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00c8f564-1432-3c9a-9e31-e2fa7df3526a | -19.72647 | -46.55965 | 2025-10-03 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce03e76-c833-3910-8cc9-fbed5b939cd2 | -19.59449 | -45.90377 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 432e4c4f-5187-39e9-90fb-e603e75cb747 | -16.33595 | -49.93974 | 2025-10-03 03:47:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de3e31f4-2f53-3e73-81bb-53e895c76e05 | -19.95179 | -46.08564 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0580330b-a6a5-31f4-a667-5a0ee1b90f06 | -17.84676 | -46.84023 | 2025-10-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67fac96f-7811-34a0-a276-e203c27f9bc4 | -16.26941 | -47.86359 | 2025-10-03 03:47:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14fa065f-8413-373d-ba33-21d6a0d743d7 | -19.59913 | -45.90461 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54dab717-0394-3337-aa45-019880f62420 | -19.72423 | -45.87342 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1998feef-6aec-3df4-9ce4-5887c1852a5a | -18.678 | -41.67175 | 2025-10-03 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| df2a963e-e3cf-3477-b3da-cc07dbf4993f | -17.1219 | -47.13114 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e98293a-c0b2-3a4f-8b32-d7170df20502 | -18.7056 | -43.18455 | 2025-10-03 03:47:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fd9a88f9-bdcd-3b86-a5d1-789736027c13 | -18.45125 | -43.81034 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 255bed2d-2b40-3407-9caa-9e2efee5ba74 | -16.81527 | -43.80053 | 2025-10-03 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6c21e18-6315-32f7-80b9-4c2c61366423 | -19.90041 | -44.51171 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 978e3d15-14d8-3644-8c3d-d332c2836d32 | -19.14453 | -43.60844 | 2025-10-03 03:47:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1bdee99a-15d3-3532-b901-684131ec862a | -19.56509 | -43.17351 | 2025-10-03 03:47:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65cfe505-6073-3d50-9346-5faeebaf6f4d | -19.85069 | -46.16537 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b972cd2-de2a-320a-bd93-f973bb8f5429 | -19.45991 | -44.27715 | 2025-10-03 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 009383b5-8fdc-3cf0-8d27-348adda2ac4e | -16.2729 | -47.102 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffbf3a98-2e11-3920-bb8f-358787384360 | -16.29289 | -45.24163 | 2025-10-03 03:47:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d580240-bc5f-3828-ba2e-091599493938 | -20.11587 | -44.39021 | 2025-10-03 03:47:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e9fb903-1ab3-3c12-ac2e-34857f973c42 | -18.45452 | -43.81572 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c1058b9-1fe4-3e8a-bf1a-c4c8bf40c2e1 | -20.12872 | -44.00885 | 2025-10-03 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 19dcc9ed-bf53-3dc3-8407-1d7bfa2cede9 | -15.23948 | -50.12564 | 2025-10-03 03:47:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3f5013d-c216-301d-88d3-89eab7ca6511 | -19.90542 | -44.50829 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 07bd6753-7f6d-3c2b-8ab5-09aa1919b3df | -18.79459 | -43.74997 | 2025-10-03 03:47:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b1b346d-ae6d-3503-a99d-16c4bc3a79ea | -19.3684 | -41.75057 | 2025-10-03 03:47:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4551761f-52fb-3ba4-9a46-97efa911fbee | -20.02427 | -41.33007 | 2025-10-03 03:47:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 321d7019-d2b6-3ea9-b6bb-6d28d25d1bb1 | -18.67755 | -41.67505 | 2025-10-03 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 72f3ce34-e500-3dfa-b513-d20ab4354e78 | -19.46469 | -43.64961 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10e84d0a-ea42-3cfa-b5c5-fdda393159bd | -19.90067 | -44.51166 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5a3994f5-3397-399c-bb58-4adcde51d1cc | -16.34826 | -47.10432 | 2025-10-03 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d4ac600-3dbe-35a3-8d4a-3c6eca2c002c | -19.72192 | -45.90937 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9c696c1-1b29-38bd-95d6-4f0b3e146a20 | -19.72752 | -46.55441 | 2025-10-03 03:47:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1b2bb38-c3b0-3482-b46f-bc7f9055c6f4 | -20.08519 | -45.80299 | 2025-10-03 03:47:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01e383f8-2b63-3471-9b9b-398c8793a829 | -16.76679 | -43.96412 | 2025-10-03 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b18de330-ebdf-36e7-8a80-6b517b7e70d7 | -19.72007 | -45.91875 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
