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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1998796-50c4-3e5d-91cb-5ce7890a397b | -3.48416 | -59.63803 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 936033dd-55ff-3178-b1d7-f93abaf38a27 | 3.52046 | -51.50552 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8cb8bd14-f375-3593-9660-6d4d3095ef1e | -3.46964 | -60.66319 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 079cfb2d-15cc-3d95-85d8-8d648333719b | -3.67945 | -60.53781 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 00288a56-3e18-394d-b73a-4b9f99f16b25 | -2.92576 | -53.94956 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 901106ec-9920-3b44-88be-287760209318 | -2.9564 | -65.20792 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4ae559b-ed5d-3128-888d-c23b67e9d5de | -2.04346 | -54.30149 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 083a217f-cea0-379a-9438-119917abcffa | -2.77912 | -54.09369 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| d2a123bc-7a00-31b8-97a0-faa8722f1595 | -2.93101 | -54.13348 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5c10a80e-364f-3b35-9977-f25703c3d7df | -2.04014 | -54.30199 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 36862b7e-12eb-3b3d-9ebf-e51a23372005 | 1.9051 | -55.72437 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4d857fcc-48f8-3e02-8f5f-f55718a2e069 | -2.32834 | -56.16911 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| fc939ee2-a10d-3000-899b-d08087f0c429 | 3.54057 | -51.50356 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fea5b2f2-3909-31bc-b497-6a3bd51d025a | 1.49821 | -55.64258 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e98f1e04-c085-3426-a484-6795af98cf13 | -3.0092 | -57.74075 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c750228-19d7-3a57-a7ef-37fc9ee5d562 | 1.86023 | -50.67323 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7c2226e9-1fef-3302-98c7-9cca2b8d47f8 | -1.22477 | -56.20554 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 85faa3a2-065c-3e6e-acb5-dd278ddbe841 | -1.67929 | -55.06092 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2d7223db-1a22-3d65-b640-50a6059e88e1 | -3.01296 | -57.91616 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed8ece76-5b58-332d-9adc-fd35bc506eaf | -2.95607 | -57.61038 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b5ecc447-ba1d-308a-bfc3-6f57ed6929ba | -1.67466 | -55.75433 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 66276ef2-5f7a-30fa-84d7-3ae82f642fc3 | -3.0398 | -65.09237 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 26ca7967-2b9d-3537-85fe-98beefe9bba1 | -3.42939 | -59.57075 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7a7da77b-5a94-3f6d-94eb-0667c6b0bc19 | -3.82587 | -64.20652 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8f7546dd-e3a5-3c5b-a655-a72c10bc031a | -2.70578 | -60.02192 | 2026-10-05 17:17:00 | NPP-375 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0be040d1-7cfa-3795-abd1-3471c21644ad | 1.73075 | -55.62646 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9dbeda0c-e4a7-39e3-ab5b-cbd6c27b0ab8 | 0.94075 | -50.8874 | 2026-10-05 17:17:00 | NPP-375 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb7cc663-9be0-3494-a884-ec9f9930b559 | -2.7779 | -54.10793 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 32ba90a6-b1a2-3d75-8224-b148ed638fd6 | -3.64838 | -60.924 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| acf0558d-b421-30e7-bb2c-4be220d9d804 | -2.26128 | -55.08653 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| aa3f35ec-529e-361f-816a-6d08f20479d4 | -1.38345 | -52.66399 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 02016295-8e69-35b0-b0c9-dd2e9979ffa2 | -1.18707 | -54.13919 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7b27c892-4eba-379e-9dec-d10d0b117dd3 | 3.52505 | -51.50123 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e63422b-c59f-36f2-8dda-be38968a26ef | -1.80622 | -53.75195 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1ee772f6-9ccc-3e5d-9fdd-90e6dd7ce17f | -1.361 | -55.98361 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cec314ec-4a1a-33bf-b573-9c66801a1f0a | -3.24201 | -58.75816 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0d6d509-4ecd-316c-9b20-fc69704603bd | -1.21801 | -54.5412 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2bed9f38-8694-3a6f-a322-b3b8355a52e1 | -1.30839 | -54.22639 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 58cfe247-9116-38d3-998c-b2a05a9d9801 | -3.72762 | -59.59903 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d73013f-fc8d-3226-81b8-68d504e6a322 | -1.46344 | -53.61115 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 079a0801-97fc-3f7a-bef9-4fbe4f275a6b | -3.10248 | -59.73964 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fba51752-03f8-3f90-a902-f1a850414783 | 1.53837 | -60.38269 | 2026-10-05 17:17:00 | NPP-375 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2e55c608-76a0-36c1-9838-cf49caa7fb07 | -1.97137 | -53.10778 | 2026-10-05 17:17:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d023445-e6e9-3f5a-8147-888c407ee21f | -2.55085 | -65.87488 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9063ec23-7dff-319b-be8b-b3b5f65f75f3 | -2.90234 | -54.12369 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| de15ae7c-0fc3-3eab-9415-f94870a975fb | -1.63349 | -55.53078 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 32882465-aca8-3399-ba59-ad163db92c54 | 1.79207 | -50.62616 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 140b29d9-2e8a-3e33-9d3f-1f5533e24e36 | -1.73638 | -55.34637 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f1a05434-bb99-3c62-b575-e66e2bcf5cb1 | -2.98321 | -54.78561 | 2026-10-05 17:17:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3be84ff-376b-3731-8b95-7e752412c6b0 | -1.76894 | -55.84433 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d80ad73-010c-36e2-bf8b-749740d11fbb | -1.88972 | -48.49991 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ea39c7b5-3937-32aa-a240-b9d88604a14f | -3.62824 | -59.32322 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8783e8a-1928-30e1-b95f-0fbd8e7749d6 | -2.77201 | -57.67411 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 307.8 |
| a03a83c3-5bf4-3397-bace-c96e227bf80e | -3.82532 | -64.20268 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6c57ba34-8d79-31d2-b54d-7d607e6f2bb9 | -2.48817 | -56.82364 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e279cc44-d82d-36f0-94ef-18e2df212a3e | 0.94103 | -50.19993 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50fa244d-8315-31f6-88f0-f998142c59eb | 1.45439 | -55.66338 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 001debaa-2fa7-3ef1-bcdd-93d20167c168 | -2.29782 | -57.08519 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ed2f1a9-d4bc-386e-af5c-7e7058cb8ada | -1.1077 | -46.64729 | 2026-10-05 17:17:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ad4a6b09-0732-3792-a42e-ee4f38bee3c7 | -0.66699 | -49.52164 | 2026-10-05 17:17:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd53f502-7ac5-3fb9-b10d-ea2606379420 | 1.16593 | -50.74498 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2c668f0-2be9-36bf-9d91-a6fb3c071afd | -2.93486 | -54.13643 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b8d4f4c3-ac52-3c63-9348-35f6f606c3c1 | -2.76774 | -57.67045 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 6c4b9498-e92e-39df-8e00-e4b2975b5b0f | 2.28304 | -59.74689 | 2026-10-05 17:17:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d177966-ad7f-3b2a-ac72-2bccc4af95c6 | 1.51531 | -55.64164 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fad30753-99d6-34e4-b6e3-6ca8363181fe | -1.55699 | -45.72683 | 2026-10-05 17:17:00 | NPP-375 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39cc75f0-aa8c-3a34-9fb7-fcaec0249050 | 3.54445 | -51.50415 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 36afd715-1ca9-358b-b459-d93106d711f1 | 0.94048 | -50.20349 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81572315-85ac-3e7a-88a1-63268e1df609 | -2.88573 | -54.12621 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c66d9ba-895b-3444-8bc0-c4f620609dd2 | -1.87208 | -50.04671 | 2026-10-05 17:17:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2cb80bd-a852-3e0b-aa84-90a79493af56 | -1.93646 | -48.39783 | 2026-10-05 17:17:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91754c75-c9b5-3028-819d-757962cfdd4e | 3.53067 | -51.51693 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 61b334ee-41bc-3ef0-93b1-9499a319542a | 2.26098 | -50.82165 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e7afc96d-e3ff-3a8c-89a4-7fdef2c57557 | -1.55168 | -45.72766 | 2026-10-05 17:17:00 | NPP-375 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d7c106ba-32d1-3575-82f8-742f22a14d5a | -2.18714 | -56.6402 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2745fe86-2b33-395c-a6d6-d275c281972a | -1.87525 | -50.04113 | 2026-10-05 17:17:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a383e22b-b4e3-365a-8e93-3fb32caf21ac | -1.19733 | -53.38702 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b9c13165-3865-3828-9fff-1905a2a9c0d3 | -1.18993 | -49.25511 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 88d9b07b-1c2d-3e8a-8469-5a59848c8453 | 3.52893 | -51.50179 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec656c04-9d31-30e8-82d2-3bd8de29e304 | -3.51092 | -59.56241 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 335f5e2b-2a06-3bde-bf7c-03bff36836b4 | -3.76779 | -59.40131 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c5c888d9-dc01-3869-b561-93cbc9027253 | -2.88294 | -54.13017 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22567889-76b2-306a-8048-4ca1e6acef70 | -3.29982 | -59.39832 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7eb84f5-c35e-31fe-874e-6063729d7dfc | -2.53839 | -65.87659 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 254427cf-7fef-304b-b8a7-0320efce3b72 | -3.6207 | -64.3409 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 74b86857-4738-335e-bad6-4466f3fcc48f | 1.57712 | -55.98734 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f2fa674-2ab8-3a78-8df6-0f3da87104e1 | 3.53986 | -51.50838 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2b899ca-5d6d-36a2-813d-d9bcb1fc672b | -1.9227 | -56.75639 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ca9aa88-9759-37d0-9825-dfd0f06f0675 | -3.17183 | -60.05696 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 87df3a74-0fd1-32e6-8f4a-9ca56f7e70a1 | -2.97251 | -54.07688 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ca2a891-31e9-35e9-a308-a11c10bb8674 | 2.25225 | -50.82558 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6681e490-40fa-312a-9121-085797afb095 | -2.26328 | -54.81042 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f1df1b60-2fe0-3da1-8686-ea1477c38d2d | -2.09159 | -48.84256 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 67cf2528-b1ac-3635-a410-4ecb4812e687 | -1.85313 | -50.62792 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a85711ef-8830-35ba-b7a4-5a1f992b84aa | 1.51689 | -55.63131 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41c4af31-81d0-3306-b178-6fb3ea7a8815 | -2.92928 | -54.14434 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1f3dbc4-2b55-34d0-9754-6d05b2378621 | 1.93425 | -55.71117 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfa0b83f-8b4c-358d-9f57-2af7727366df | -1.61527 | -55.10667 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| aa7181f2-621a-3895-8dbb-b7e414b2c710 | -2.07621 | -56.83386 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 94fbcb0e-8be4-329e-b7a2-a18a94faafdf | -2.85724 | -53.91827 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README124.md)
