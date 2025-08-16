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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c05fce33-7fb9-3b71-b3a5-f28de2e0189b | -9.16083 | -59.63275 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a64e2b9-7273-39bc-8f2c-e8a4fbf8b141 | -8.97575 | -61.70523 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da9e7a4c-224f-3aeb-b74f-52d87ce96cf6 | -9.18838 | -59.68605 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4e57b9a-2a7c-30d7-b7db-8c339e7259c3 | -8.99122 | -60.51448 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15e97bcf-83c4-3f73-8761-e5fc134ae929 | -7.03834 | -59.62109 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 655ae145-8477-3db6-bdc2-4b3f25fa89c8 | -6.63091 | -60.01662 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8587f3be-e62f-3fde-8538-2eb4f3535032 | -8.06076 | -70.58119 | 2025-08-16 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 710f57a0-32e9-34d2-9c59-25304ed7abb4 | -6.94308 | -59.53348 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f980419-b647-35ca-944f-772ec3a66139 | -9.16706 | -59.63747 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e62f58f0-1d67-33ae-803e-6b14f25d7795 | -10.96613 | -49.57103 | 2025-08-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3d1266da-6059-3929-9c46-76f664e4ec00 | -8.15189 | -62.77163 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83fe4095-c24b-3561-a493-baf44e2eccfe | -7.92851 | -61.74478 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 334ac610-8efb-335d-bc5d-cd9b72c98d9b | -7.13134 | -59.65694 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19fefe54-1229-3391-8f19-4d92b5c99fce | -8.89854 | -60.74058 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a6d1e9c-91f8-382c-bbc3-6e1dbd7ada92 | -7.46003 | -60.41446 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89c1ad26-8b0b-3109-bf7e-ae7bd249499d | -7.56441 | -61.42168 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efcd6247-16dc-3365-a700-da9f3d54d89c | -3.23266 | -50.80613 | 2025-08-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f7afe2-32ca-3b84-82ca-77895ba608db | -6.9362 | -59.64556 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 972e7a1c-575b-3f90-b4ec-fffc131716d5 | -9.16536 | -59.62589 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e04a8755-2c64-34ea-9411-bdef938451dc | -7.61102 | -63.33927 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81798447-252c-33c1-bff9-4cc6b137c95d | -8.11443 | -61.18972 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8312788d-f962-3d02-8ef1-2edd4ffea65b | -9.17216 | -59.64957 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fac1ac71-7dd1-314d-b282-fc34a4521c4d | -9.04849 | -67.42986 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5e2b417-77e0-30e7-9e1f-1fc9d5015013 | -6.94815 | -59.54525 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9adaf257-3a17-3ed1-9d33-2c3c9c234e09 | -8.92777 | -60.72725 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe323182-38e5-3bb8-b852-e7313a2d1350 | -9.5097 | -60.54517 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6644bf40-4202-3bb0-a193-5f9d0d7a99cc | -9.5025 | -60.54767 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46f64b9f-f586-31cf-866b-bf22fd381cc9 | -9.1637 | -59.68216 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63b2cbcf-901f-3675-901c-3a8c05f97466 | -9.04419 | -67.42912 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc867dd7-3eeb-35cf-b723-4839754f3b14 | -7.61225 | -63.33157 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7bb5679-5c4f-3076-89f8-c1eefe1a349a | -8.99448 | -60.49335 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d537ee0-f929-303d-bf43-ebc3fbb59cb2 | -7.28845 | -60.62192 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00a9e641-6125-3656-a206-c0179832ab40 | -6.4846 | -62.93491 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc700394-77de-3bfa-82a8-42ad1597c128 | -9.06028 | -58.94632 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e85955a-c7e6-3227-bd34-cb5d5edc87ed | -7.5974 | -63.50005 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dcb27ff-b856-3dc6-bcf4-4b5478c5cec0 | -6.90986 | -59.61598 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0e87ace-3975-32df-88a0-485b80f24d87 | -9.50629 | -60.52291 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ad67445-f804-3a6b-8116-bd348d2ba407 | -3.43453 | -49.05144 | 2025-08-16 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 968b9635-cc0f-354a-89ad-c63c2025997e | -7.92519 | -61.74426 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff4e28b8-73da-37a3-9cc4-0113177b8398 | -6.79667 | -59.82315 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54c32657-1935-32e9-b42b-266680a7fa0f | -7.07404 | -59.22797 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce79a34d-5942-3395-9d94-68792ebd8047 | -8.97417 | -64.22341 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04e4d907-02d1-3465-9aef-58b792453038 | -9.63163 | -63.09265 | 2025-08-16 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2db924cc-3b97-3711-a5fa-3c4fc89d0c3f | -7.2768 | -57.65903 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a492c72e-0b1d-3d30-a441-1c6ebd6737b0 | -8.90957 | -60.73514 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be5164ec-7025-3117-8325-91fb85e24b82 | -8.98898 | -60.50691 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ee0a7e3-c373-3f52-bf74-2bf84ea2d714 | -9.16479 | -59.62957 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a31e34f2-47a3-3821-adf8-70977c41804f | -9.18261 | -59.65506 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26cd791e-297f-3e94-9d24-71ba9e55f803 | -6.48522 | -62.93112 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd880313-46ca-39e0-9843-2abd27fc4f81 | -6.63531 | -60.01014 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 305dd078-a941-330c-9df2-f1f414a45695 | -7.68397 | -63.3194 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21650beb-1e9d-34eb-8e7d-eeb6178fa7d3 | -9.20972 | -59.63659 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 08f95cb3-fe06-33c1-acce-1ad5359d4845 | -9.00072 | -60.54118 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a1e0be-a0b1-3953-9542-34108cd62236 | -6.62588 | -60.00508 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c228a9e-9e76-3bbf-b173-055f6c34e0cb | -9.92098 | -63.1882 | 2025-08-16 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33fd2b72-5684-3d93-957b-e3d211010ddb | -2.37917 | -47.6673 | 2025-08-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b17e6d0-9531-3276-8f8a-25aeec3ddadb | -9.1631 | -59.64065 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb9f0223-0df3-3c7a-8dbc-3b36f1968666 | -7.61286 | -63.32772 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db61c55-dd82-3ebc-9ac1-f0a8b5ff93fb | -6.94534 | -59.54116 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68d8a3fc-446b-3a82-be41-b1676889c2cd | -9.16933 | -59.64537 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1be61aa-4abf-35c6-b033-1cb79320f6e4 | -7.32898 | -59.62893 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f61ad795-e4cb-3c10-b645-ce6904b6eeb3 | -6.9437 | -59.55188 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef2e7f5e-f251-33ad-8a78-74218abe51b6 | -9.15856 | -59.62486 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0aba536-accb-3cfc-ac74-be5f28bbcb75 | -8.98857 | -60.55368 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7c71c4f-bd54-385e-a683-b9ecb14c7145 | -8.9957 | -60.5296 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ae26b4c-7250-3a08-8da2-ae597bb5a2c5 | -9.20181 | -59.64297 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34562eb9-3dfc-3e81-8930-40b345a2f580 | -6.48053 | -62.93815 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9b36fd8-a53b-329a-8c50-7c62bd59bf2c | -8.9978 | -60.49387 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f8cf148-c3e5-3bc9-87ee-48c7b21456ab | -6.93418 | -59.54671 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33c8c35f-ac17-383a-9e4d-5f2c51e67650 | -9.20008 | -59.63137 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4613e527-72b2-34ed-9a59-ca168f1c6328 | -6.9295 | -59.64449 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fa6b2f4-cbc8-36f9-ab95-62a3f47cf93c | -7.12744 | -59.65998 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebcfd5a-871b-3392-a6db-b0b37ab9bc02 | -7.04559 | -59.61858 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75ee216-d7c2-37ff-973c-01c354bb7381 | -7.07971 | -59.23631 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a188bb26-c1dc-35cc-b62b-aee627cc02ce | -9.16028 | -59.65907 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a43492-bf68-3cd3-a5f1-d014e9ddea87 | -8.80849 | -52.07372 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10e9a895-8370-309c-bb78-e55c43a3d2a2 | -7.43212 | -60.0228 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd1088f6-e0f9-3ab8-b0b1-1a99358c7bc6 | -7.95341 | -61.75949 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d3195b2-a1a2-308d-b264-142f714873b1 | -7.6143 | -63.33182 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b403a723-90c4-305c-b4ae-a19308b18b6b | -9.15692 | -59.68109 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5dad4f4-b202-35c8-af65-8613176483b3 | -7.61493 | -63.32798 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9352550-5257-384c-ab52-567bdec53faf | -6.93691 | -59.52884 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4df3679-066c-3c7f-9b7b-23001c68a9b3 | -9.50475 | -60.55524 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10cbb52e-c276-3aed-91c9-a3b96abb5494 | -9.158 | -59.62854 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a9258b2-c233-36ae-a3df-6b0c06753e4c | -3.65274 | -48.32479 | 2025-08-16 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c3d994e-3279-34cc-9734-f35a3cf36307 | -9.50684 | -60.51937 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6076c43c-2712-35dd-bd6b-43fe060b5bc9 | -7.53506 | -61.34948 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362884eb-95fd-3c65-877c-e0afd27913ec | -6.9418 | -59.65371 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1ea1a04-bcbf-3ca8-91e9-7645a146de7b | -7.82747 | -61.32875 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a8bef4c-b8e9-3f40-bd89-4e259d85bc89 | -9.50141 | -60.55472 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 81d07079-5656-3783-a7a8-4609fad5f591 | -7.32977 | -60.61771 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0725372c-80e9-3028-aed4-4f7fe144f6d7 | -7.06955 | -59.23472 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec79f24d-48fb-340d-8438-c8e5083be8b8 | -9.15743 | -59.63224 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2faf0e1d-fbd5-3aa3-a996-cf6c01a67dcb | -9.16876 | -59.6264 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b7f879d9-1e94-3eee-879e-797f9c8a2f95 | -7.49732 | -63.82217 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5a2b6e02-5d7c-3ff0-8cab-f5a5736f0db1 | -6.80001 | -59.82367 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c431719a-e18d-37ac-a299-0d536aa9d263 | -9.16366 | -59.63696 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bbbcf3f5-660e-37bd-afcd-6c721c5644b3 | -6.91103 | -59.63073 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbd87933-f211-3b00-b8ec-8d6aea22776d | -7.9501 | -63.21655 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2582b4e0-b156-3851-8f61-2bb11d73dc5f | -9.50467 | -60.53353 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README58.md)
