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
| d2f7536a-c98b-3bf1-b503-0a5a7babc242 | -9.1715 | -59.5599 | 2025-08-27 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a74a575c-9b6a-38f2-a492-5b9273d2e109 | -13.1837 | -45.2865 | 2025-08-27 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7b3d8995-dedd-38cf-938c-f8fb42247b63 | -9.1529 | -59.5609 | 2025-08-27 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4c28326f-63a2-3c74-9287-b1248deb0e0a | -9.0821 | -49.5638 | 2025-08-27 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1e57c44e-0ac1-3b64-ac16-a0e752d11ab6 | -9.7915 | -64.265 | 2025-08-27 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bae8f66c-b21b-3662-b914-e4adb3e0df09 | -6.8412 | -58.9746 | 2025-08-27 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| aac70919-daad-36b1-bd60-08f549440990 | -6.8228 | -58.9753 | 2025-08-27 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 7019706d-2d7c-364d-b2fd-77d0d196747e | -9.4062 | -60.5326 | 2025-08-27 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| cac05871-d524-3e7b-b8a9-a71ec2aacd3c | -9.4065 | -60.4941 | 2025-08-27 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| efd73022-33a7-35f6-8607-f7ec2ccf72bd | -9.1007 | -49.5835 | 2025-08-27 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 19a5ce1d-fd4b-33fd-96d8-d31c339fe703 | -9.1009 | -49.5621 | 2025-08-27 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 953b2dfc-60d7-3742-97c5-ad23fc41a4d1 | -9.4065 | -60.4941 | 2025-08-27 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| eab1a3df-29d5-3862-a002-52d1394653b2 | -9.4062 | -60.5326 | 2025-08-27 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| f7a87b96-09f9-34f9-bba1-69bcaff981db | -13.1837 | -45.2865 | 2025-08-27 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b5833a0f-5557-3acc-9325-86ca5bdab04d | -10.2743 | -64.4907 | 2025-08-27 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| f9c50d69-147d-315f-8672-13438d9e32b2 | -9.4064 | -60.5133 | 2025-08-27 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 3a7b994c-a40a-35c7-a811-9f1339499a7c | -9.8101 | -64.2642 | 2025-08-27 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 1dea9917-7d9c-332a-ba60-7305e3db58dc | -20.7074 | -49.2447 | 2025-08-27 02:40:00 | GOES-19 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| a39a518e-c3ee-3170-abc9-9eb0652e55cd | -9.1009 | -49.5621 | 2025-08-27 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| bc74b2a8-344e-3b22-b141-9a7f2e575105 | -20.6869 | -49.2492 | 2025-08-27 02:40:00 | GOES-19 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.7 |
| 4d5b18b0-0d05-36dd-ab4f-dbdc1140fab4 | -6.8413 | -58.9552 | 2025-08-27 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 6043f262-22e9-316d-8df8-7d9ae20dc9ad | -5.118 | -43.2198 | 2025-08-27 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 1fe73b73-32b1-3c6c-99d1-280d4fb3a177 | -9.1715 | -59.5599 | 2025-08-27 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0edb8be0-0379-34bd-baeb-decb1fb42ca7 | -5.1181 | -43.1964 | 2025-08-27 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bf7a5b92-6754-3804-ad0e-82ce32a04fef | -6.8412 | -58.9746 | 2025-08-27 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 14fb543b-b4b4-3fb7-9fcb-fbdb35c84d15 | -9.1529 | -59.5609 | 2025-08-27 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| eff14bc3-fccc-34ec-81bd-fd5c8b1d3b6a | -9.1007 | -49.5835 | 2025-08-27 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 184e1126-ec0f-34e1-a362-731d59a3682a | -20.6863 | -49.2722 | 2025-08-27 02:40:00 | GOES-19 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 420bfb45-3242-3d5d-831c-8171425d0b88 | -6.41071 | -35.04014 | 2025-08-27 02:43:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6c1e43f4-6d1c-3b66-925d-d26d624a6c64 | -6.40932 | -35.04749 | 2025-08-27 02:43:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b0050602-3bd9-3c95-b0fc-bc58e22abcbb | -6.40795 | -35.05479 | 2025-08-27 02:43:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fabdf34f-2bb5-3752-a1c2-d3e5aed9ce7c | -9.4064 | -60.5133 | 2025-08-27 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 4ed8c410-d0fb-3b7f-810c-d1633193549c | -12.9068 | -44.658 | 2025-08-27 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 84ebb3df-5ae1-3ddf-b4a7-95786dba5953 | -5.118 | -43.2198 | 2025-08-27 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 019cc602-89df-3dc2-8c50-08dcfe16d98b | -9.1007 | -49.5835 | 2025-08-27 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bbf34e4a-1c10-3e18-aba3-45e930a274c1 | -9.4065 | -60.4941 | 2025-08-27 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 0a80be4a-6e3a-3fb0-933f-6920c1d78bde | -20.6869 | -49.2492 | 2025-08-27 02:50:00 | GOES-19 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.4 |
| 46d49c3b-fdb8-344c-a5d2-7a0e93c4d9cf | -9.7915 | -64.265 | 2025-08-27 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 4599bfa6-39c9-373e-be32-8462bec2a383 | -9.1009 | -49.5621 | 2025-08-27 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c5d805c8-f24e-3d25-9d14-4d507f446eaa | -6.8413 | -58.9552 | 2025-08-27 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2585e7be-ae6f-3d0b-86c4-daeffe5ebfc4 | -9.0821 | -49.5638 | 2025-08-27 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8d0fffc3-4542-35a9-a68d-120de2377a27 | -9.1715 | -59.5599 | 2025-08-27 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 398b8bac-4c5d-3717-9a25-f6eefcb5b820 | -9.0819 | -49.5853 | 2025-08-27 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a3340de4-06fe-3fda-9298-b607432d4f4e | -6.8228 | -58.9753 | 2025-08-27 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 15b96687-8aef-32c7-a408-b5db99d6ddd7 | -6.8412 | -58.9746 | 2025-08-27 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8937e375-b421-387b-a266-bce37fcd8bca | -9.4062 | -60.5326 | 2025-08-27 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 56b284c4-1295-344f-b39e-9c35c87f5eef | -5.1181 | -43.1964 | 2025-08-27 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 51f0d6d0-b04b-3683-9395-49457d6526f1 | -13.1644 | -45.2897 | 2025-08-27 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f00ef2a7-7e8f-3049-9eb4-8febbf73c8ed | -9.4065 | -60.4941 | 2025-08-27 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 058dae19-d57a-3549-83c9-a13987ece3f8 | -6.8413 | -58.9552 | 2025-08-27 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 61565b29-276a-3aa9-bcd2-2fc3f51f29a1 | -9.1715 | -59.5599 | 2025-08-27 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 66ed73d4-109c-3a39-b5df-a31df092f3a3 | -12.9072 | -44.6346 | 2025-08-27 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7fce3b37-8517-392e-abee-8467bd14afda | -9.1009 | -49.5621 | 2025-08-27 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a23837fa-2f4f-33a0-aa68-8aedbb972fa3 | -6.8228 | -58.9753 | 2025-08-27 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d99c81f4-3866-3218-a563-9c9748035f6c | -9.4062 | -60.5326 | 2025-08-27 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| b8927810-3db5-34a9-a6ed-4c70cd9fee80 | -6.8412 | -58.9746 | 2025-08-27 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5cd0f807-1eac-309e-9755-d95ed4e87c0d | -9.1007 | -49.5835 | 2025-08-27 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4a30e880-e710-32cf-8d99-567c2e2323ff | -12.9068 | -44.658 | 2025-08-27 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 433b8521-9004-3a52-8291-7570043600ff | -9.4064 | -60.5133 | 2025-08-27 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 79aedcca-ea41-3e77-b078-d2a4ea923b92 | -9.1715 | -59.5599 | 2025-08-27 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6cba52d2-8b2b-33ea-90a2-a668b3276290 | -12.9072 | -44.6346 | 2025-08-27 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 2b5a490c-4654-30ad-906a-47034145cb14 | -9.1007 | -49.5835 | 2025-08-27 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d9f54dc0-ff8c-3810-ab5e-f4bb6cea7dc4 | -9.4065 | -60.4941 | 2025-08-27 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6de6959a-600b-38ac-bf36-662b2c821614 | -6.8228 | -58.9753 | 2025-08-27 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 354a2e18-ee79-3894-a0f4-1d9fa35f5bef | -6.8413 | -58.9552 | 2025-08-27 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9358a59c-899e-3509-addf-0bedfa832524 | -6.8412 | -58.9746 | 2025-08-27 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 91594c93-443c-39da-8fde-21aedb153da4 | -9.4062 | -60.5326 | 2025-08-27 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| bdfaa8b4-9de1-3814-bd82-b901a67eaa7c | -12.9068 | -44.658 | 2025-08-27 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 89d82e38-1d51-36dc-a701-efb3dbe35825 | -9.4064 | -60.5133 | 2025-08-27 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| b253eb38-f84d-3c7c-8ee5-3418a343cd00 | -15.748 | -49.9586 | 2025-08-27 03:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 05aedccc-1330-3a55-a470-9d53a3b816fb | -9.1009 | -49.5621 | 2025-08-27 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 06718754-a819-3acc-ab55-02c5f5d6c32d | -12.8879 | -44.6378 | 2025-08-27 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1c741835-4752-34ed-a089-cc6efff8e53f | -13.3943 | -51.7595 | 2025-08-27 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 940f95d4-a7ff-378a-a882-d876e21cadc3 | -6.8413 | -58.9552 | 2025-08-27 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ee213f9c-c0ea-3a2f-a1a8-734a1f575cb5 | -6.8412 | -58.9746 | 2025-08-27 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a0f08702-9c3d-32c4-a830-f414d629ebb8 | -9.1009 | -49.5621 | 2025-08-27 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 161a8807-3871-3cfa-88b3-f1b5bfeec6aa | -15.7284 | -49.9617 | 2025-08-27 03:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e0158c13-1cd5-3fc0-8a5c-ec1f242e7140 | -13.4032 | -46.8987 | 2025-08-27 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1bdae0d2-cf1b-3cc5-a5ae-9e97610de878 | -9.4062 | -60.5326 | 2025-08-27 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| da573ca9-4725-38ad-aa8a-bccfa06392a7 | -13.4027 | -46.9214 | 2025-08-27 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2c1e7bf4-5e79-3ccc-b473-9cc73e27b58e | -9.4065 | -60.4941 | 2025-08-27 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 056a6193-ac1e-3e12-b9f3-d0e5bd17563e | -9.1007 | -49.5835 | 2025-08-27 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e45c61e9-721e-39c9-9f14-4887e655261d | -15.7484 | -49.9365 | 2025-08-27 03:20:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 49405573-ceae-3437-9433-5bd8fe472c01 | -9.4064 | -60.5133 | 2025-08-27 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| c9787766-c9ff-3b98-b899-0b2e8afdd7df | -15.748 | -49.9586 | 2025-08-27 03:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 346.6 |
| 437c4ee8-01d5-3999-bceb-34e985db7e72 | -9.1715 | -59.5599 | 2025-08-27 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 76e00198-b62a-35e0-8752-17168e4355bd | -6.8228 | -58.9753 | 2025-08-27 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c842910d-b3dd-3dcb-990f-d1e425c25d4f | -6.8228 | -58.9753 | 2025-08-27 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 1d058b50-0bcf-3814-93aa-ea758770737b | -6.8413 | -58.9552 | 2025-08-27 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 39221077-3fdc-3d72-ba00-ce83cc6817ff | -9.4065 | -60.4941 | 2025-08-27 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b69f5706-eed8-34f7-b283-84408c2e1e07 | -5.1181 | -43.1964 | 2025-08-27 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 9af7fd54-bfff-3255-9085-ccb9f9499ac5 | -9.1715 | -59.5599 | 2025-08-27 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ef4d640f-597b-3581-8ccd-f1511f812f18 | -9.4062 | -60.5326 | 2025-08-27 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d199444c-09be-34ad-8103-30a4497ff480 | -9.4064 | -60.5133 | 2025-08-27 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 202fc87e-cb5c-3c50-bb9c-bc1a49f7593c | -5.118 | -43.2198 | 2025-08-27 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 9f55aecd-8611-37d3-80be-31df371a9654 | -6.8412 | -58.9746 | 2025-08-27 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f7cf7c62-5778-377d-bf0f-73fc77774295 | -9.1009 | -49.5621 | 2025-08-27 03:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| eba0c64f-51a5-3c27-bd5c-b3b7e1dd4d4b | -6.84151 | -42.82141 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d24dc496-9b4b-3a75-a6c6-44bf56616ae5 | -6.32109 | -43.60849 | 2025-08-27 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 833260c5-bb6e-333a-994d-585f62cabb83 | -6.96085 | -44.09106 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
