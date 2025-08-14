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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f74528cf-d212-3e06-b8cf-df69cb8e0333 | -9.50879 | -60.5428 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c608a936-fdf3-32d1-ae87-5d24be8880de | -9.15917 | -59.67249 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e30f1968-e83c-36e8-9365-134909a79398 | -6.93844 | -59.63809 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9558386-9b02-3c9f-b087-1e493b00784b | -6.87642 | -59.15343 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d65f0e7e-d5f9-3e9e-9aa0-fdfd1dc5a993 | -8.10511 | -61.20746 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e5c4ce6-59aa-3604-b99a-6ba8546b9837 | -10.75791 | -69.08644 | 2025-08-14 06:01:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8481fb-e1d7-3ccd-82d4-51d0356eb514 | -6.91112 | -59.63284 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e294d4c9-e631-3c9d-b005-e522ad0cff28 | -9.50502 | -60.5258 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b30bb46b-9b2c-35ce-9402-a79703341f6c | -8.11322 | -61.214 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8ca5f79-20b2-3101-a1b6-aa2f135bfaad | -5.74365 | -59.89481 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 042b4149-1d1c-3465-aa0e-7bde3c1fa41c | -8.10602 | -61.20044 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1ca097d-ea2b-3e82-9395-24de6dc0b926 | -7.316 | -60.62199 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 269431e7-1fec-3f06-91ed-d0d9261dde62 | -9.49872 | -60.52915 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10196b0c-fa9a-3901-8414-d5ae5e4bfd0b | -6.09714 | -59.94981 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b88feaae-005d-3ab4-b5c6-b6036907360d | -5.75561 | -59.89271 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2858e24e-64d3-3d16-8d81-07bcc6f10d70 | -7.08961 | -60.01963 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb1ab41e-020e-30ee-a397-d37016709211 | -9.06267 | -60.65676 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b2ca25-1d9e-3c84-8d2a-47e35e0e65b4 | -7.97947 | -70.03857 | 2025-08-14 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1b0cccc-428f-3419-a916-e2f29979615d | -9.13661 | -59.65539 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b8d1ae7-e3cd-3a51-a559-2ff3b26c660c | -6.93957 | -59.62938 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7b629cd-6923-302b-b018-01d6025e3f4a | -9.61913 | -67.30447 | 2025-08-14 06:01:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e05a2f07-aafc-3cbb-a5a0-af763cf14bc7 | -6.9035 | -59.13094 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 950b95f7-f811-34da-b1b7-e97baf9a531f | -8.10925 | -61.20259 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43dc7404-aec0-331a-ac5c-82d4cbe9c664 | -9.18433 | -59.67884 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a971f9b7-8322-3939-9e86-f4d3e17f2da6 | -10.00746 | -59.21842 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfda9a33-eeec-372a-b258-594b131c426c | -6.91507 | -59.13736 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3923cd2-c5e3-366f-8ca0-28f4412d78ab | -7.46234 | -59.88887 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de8b7ebf-e14c-3173-a770-47d73bf080dc | -6.94128 | -59.63276 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc4f5ea8-a4a9-308a-a2bd-9089b0c62636 | -9.06367 | -60.64884 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 814980d8-9064-3bd4-bb60-afbb12771f23 | -9.14328 | -59.65161 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 643baaac-654f-3d20-9ab3-1a13267c22ad | -6.89968 | -59.15887 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 735274b9-b9b1-3587-affa-4353e727156c | -6.90706 | -59.15033 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| be8b522a-49d8-33fc-a4d1-abeb18609cb6 | -8.11144 | -61.20121 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8d26de7d-291a-30eb-86af-a7bcfd56bce3 | -7.32666 | -60.62722 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d981103-819f-34dd-8470-2e26e27a5683 | -6.10559 | -59.93085 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1ecfea-510f-3652-8424-4fdf7ea57bdf | -9.16464 | -59.67805 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e12d973b-2742-32bf-8f3f-f1dfe0217db1 | -6.88876 | -59.14779 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 35f15e3c-f39f-3dca-a1b8-dc2aa9d6a6c1 | -8.10736 | -61.18994 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f440b3f8-1587-31a2-9655-29db56a9b552 | -7.32616 | -60.62302 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 049c1afb-f145-36ca-94c8-138928cccd64 | -6.89533 | -59.1513 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 67696fb5-f2ff-3b51-bb68-84ab548b34e4 | -6.89165 | -59.13165 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05f31a01-2861-3507-9498-9ae94cd402d1 | -6.90815 | -59.14828 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 53da40e2-3a5d-328e-8c7a-819c21326e00 | -7.52774 | -61.38194 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1558fc9-53f1-3863-b970-0ffb086e0fac | -7.14272 | -59.65811 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1d9d3a0-7ee2-37cd-8e09-7d58e54aadf6 | -8.10573 | -61.18783 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ff060c0-570a-394a-bc9b-1f2355e73807 | -7.26378 | -60.00396 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 615a7541-72bc-3b32-8779-4cf9c4d3e1cb | -7.32715 | -60.6236 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 407e648c-8094-3c32-9442-d7a311a4f1fb | -7.13789 | -59.6488 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08203b2d-5670-33a5-a13e-121e34e09471 | -6.09768 | -59.94587 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e29b13b-8241-35d3-a9ff-d9ada021b141 | -6.87591 | -59.15091 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 613d8a35-b9e5-356a-909f-9476b4ff37df | -6.92642 | -59.1511 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b281ca8d-32be-36ea-8b8c-f3615e4e6660 | -6.89004 | -59.13837 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 953a275e-2a16-3859-babb-2f45f8dd366e | -10.34033 | -64.45512 | 2025-08-14 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b6ab51-5463-336b-b5e2-0c10bdccb6ea | -6.09362 | -59.93283 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 305f4e49-fdea-382f-b1b4-57467189dc4f | -8.11419 | -61.20689 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9c3ec71-6aa0-3210-95d8-8efc94fe6380 | -6.89067 | -59.13378 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 506ebc93-d0b1-3982-8ff8-cd5e5fb16cff | -6.11296 | -59.9199 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b799c657-dc13-3252-ace2-d10971e57b04 | -6.8956 | -59.1462 | 2025-08-14 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6cc76a88-be17-36bc-8549-f5bea0fcc710 | -6.8955 | -59.1655 | 2025-08-14 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 52585b42-d30f-3268-9ca3-c0dade7ab739 | -6.914 | -59.1455 | 2025-08-14 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 607a0e53-f93b-3383-be8c-4410bcc98d5d | -6.8771 | -59.147 | 2025-08-14 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b72c7bfa-4ac1-3e40-a731-80e9c1168039 | -23.0397 | -52.1398 | 2025-08-14 06:20:00 | GOES-19 | CRUZEIRO DO SUL | PARANÁ | Brasil | 4106704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 84.5 |
| 4272d62a-c35b-38b8-a118-15e800dc7192 | -6.8955 | -59.1655 | 2025-08-14 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f68567d0-80a4-3851-8894-7dd2d60910ee | -6.8956 | -59.1462 | 2025-08-14 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| e566783d-5e1a-3fdd-af04-4b128f4fe06c | -6.914 | -59.1455 | 2025-08-14 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| cc582ab9-7a25-3ff5-8630-306fd91c8f05 | -23.0391 | -52.1624 | 2025-08-14 06:20:00 | GOES-19 | CRUZEIRO DO SUL | PARANÁ | Brasil | 4106704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.8 |
| e5d24d63-c0a0-3d33-9d12-e7ec8eb6e178 | -6.8771 | -59.147 | 2025-08-14 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f49738f6-d5cb-365d-8d15-02879e96bff8 | -7.60548 | -63.51455 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31691c32-a5c7-32a6-9193-e204fbda6761 | -7.59945 | -63.50737 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aa06b04-f7de-399f-8772-8e497d7c09e4 | -7.60558 | -63.52042 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e07ac12e-ded6-36eb-b8dc-6d5639d2ecd2 | -7.61919 | -63.51639 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 143e9aec-aa63-33c3-a64f-b19f2fe74472 | -7.6003 | -63.50696 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dca010c0-916d-337a-99f4-71f8e45d5f57 | -8.65559 | -70.75185 | 2025-08-14 06:27:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48c7c337-7d60-3dc7-83d5-0b9fcb8de4a2 | -7.56073 | -63.48317 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fab8c0e-8b82-37b9-a1e1-7a0c71c5fcd8 | -7.55386 | -63.48224 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0efa3afe-849d-3de1-af79-dbbdd73b763c | -7.62695 | -63.51699 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aa71d72-bcee-33e9-a2b9-5b47f72e0d72 | -7.62008 | -63.51607 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 499dd218-6b2e-3445-a841-5ee9ad5f7336 | -7.61835 | -63.52264 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e101af1c-4b6d-3c6f-a211-ab6889368d96 | -7.61243 | -63.52137 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9af0b970-410b-3c66-86e7-c5e79783667a | -7.60464 | -63.52079 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad02e9e1-0c4c-37c2-9cf1-e659902ea552 | -10.06137 | -67.7471 | 2025-08-14 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37fc380b-6985-3895-a107-5933b6d1a6f4 | -9.37395 | -67.76705 | 2025-08-14 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66e32329-b013-31ab-aa70-46c7fb5da5f6 | -10.33485 | -64.46419 | 2025-08-14 06:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9511036-b420-3117-80bc-9f7f522b7a0b | -7.60637 | -63.51418 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e25c6df7-dc2a-3df3-aec7-96d058165966 | -9.55666 | -68.58033 | 2025-08-14 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ce53e8-15fa-313b-a8f5-a7a606919c68 | -7.61929 | -63.52232 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10157483-8143-32d6-bfe6-4bca6e3f99a2 | -10.33559 | -64.45822 | 2025-08-14 06:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a7062b1-6815-3231-a9b6-ea4a09e18a3b | -7.62615 | -63.52323 | 2025-08-14 06:27:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a0c5898-8c6a-3d94-bdc4-8b87811938b4 | -9.37349 | -67.77043 | 2025-08-14 06:27:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f6c3d2d-86b0-33c5-a308-2748cdf58d2e | -10.43214 | -67.7291 | 2025-08-14 06:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b6de122-2ee8-335c-976e-cd570295ffaf | -10.43167 | -67.73264 | 2025-08-14 06:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dcc4ba2-9092-3aaf-9fcd-87f9ea69bc1e | -10.43296 | -67.73165 | 2025-08-14 06:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3eb8b3e-6e1c-3949-8603-e04e5eafa32e | -6.914 | -59.1455 | 2025-08-14 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 343b4765-36fd-3fdd-9dfe-d706af95e0e5 | -6.8771 | -59.147 | 2025-08-14 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0c24a2ae-bede-391a-af11-dac84b03ddaf | -6.8956 | -59.1462 | 2025-08-14 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 6d24d414-a358-3361-85bd-d750463ed8ec | -6.8955 | -59.1655 | 2025-08-14 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a333efea-a13c-3520-bf34-e50d36d560c3 | -6.8771 | -59.147 | 2025-08-14 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c87f4808-d024-36f1-b5ea-d56d9e513ce6 | -6.8955 | -59.1655 | 2025-08-14 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 36d757cc-0695-368a-a9e2-bbbf42301dff | -6.8956 | -59.1462 | 2025-08-14 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4db7d8d8-ace3-34c5-ac48-60f3844d357b | -6.914 | -59.1455 | 2025-08-14 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |


[Clique aqui para ver as próximas entradas](README39.md)
