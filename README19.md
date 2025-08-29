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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 014815b0-a4ef-3d80-992a-a2739518f8ea | -9.7915 | -64.265 | 2025-08-29 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 97924713-2138-35e6-9b88-aefb155c4c46 | -6.9867 | -59.3354 | 2025-08-29 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5044e0c0-b870-3790-b230-7dea370d5039 | -13.1837 | -45.2865 | 2025-08-29 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b624b03d-9c95-3629-ac79-2212bbabe465 | -13.2031 | -45.2834 | 2025-08-29 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 39f3549e-5d1b-31c8-9e81-02ed5e862f2a | -9.4618 | -60.5682 | 2025-08-29 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| b41490fb-e34b-391c-8b47-c9a7ef8d0672 | -9.1154 | -65.7886 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 78b630d8-f683-3622-8585-23b5d7e8fb09 | -9.462 | -60.549 | 2025-08-29 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| ce4114c7-8106-380f-be1b-5b921f0b631d | -5.6268 | -45.0025 | 2025-08-29 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| bee40f86-9124-3e47-95da-83840a31f71e | -9.1155 | -65.7699 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 81011fa1-6605-3b20-942d-aeb83a55f997 | -9.171 | -65.7869 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f7917dd9-1111-371d-a74c-bb8f3052bc53 | -8.1758 | -61.3755 | 2025-08-29 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e0fc664f-b588-3c6a-b05c-f4251f3b7bd3 | -9.1156 | -65.7513 | 2025-08-29 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e8285f74-0347-3f51-ab84-b5d71ea9a1a6 | -6.7074 | -49.4561 | 2025-08-29 02:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 50ce31d5-cb05-3130-acf8-ca1d981d7396 | -3.4254 | -49.0517 | 2025-08-29 02:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5c8aa70c-e121-3520-bac6-c8df10cd7bed | -6.5546 | -43.9221 | 2025-08-29 02:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 204bf2e9-c9cb-3874-a49d-39b836478c5f | -13.5386 | -46.8775 | 2025-08-29 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| efaa5254-05a0-3ca3-926d-2b552efb69b9 | -9.7728 | -64.2657 | 2025-08-29 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 03b59c14-b54c-388b-b0a6-41fad472c981 | -9.773 | -64.2469 | 2025-08-29 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.5 |
| d61bea2c-51b3-33ab-bebe-f4df4af111ab | -9.7916 | -64.2461 | 2025-08-29 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 283bcfaa-7c33-37d7-9909-09b9870701c1 | -12.4345 | -63.9173 | 2025-08-29 02:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 19096093-b419-3d2f-a978-18e006ef69dd | -8.53105 | -70.74751 | 2025-08-29 02:28:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8b354a5e-7434-3bce-aa54-1211dd0cadbf | -8.53458 | -70.76037 | 2025-08-29 02:28:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f16ef90e-d18d-3465-9122-4c51435af797 | -8.53149 | -70.74101 | 2025-08-29 02:28:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 40ec9fe1-d915-34c3-9002-5c1394685e8c | -10.3624 | -57.8258 | 2025-08-29 02:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6c64e17c-e027-3e7f-b4e3-11d6dfa27c17 | -12.8413 | -48.1685 | 2025-08-29 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| d5851061-e735-317d-83fe-38b635ea44d1 | -24.1648 | -49.5569 | 2025-08-29 02:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3fee0372-dc8a-3cd8-96e7-893c02c22f99 | -9.4618 | -60.5682 | 2025-08-29 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a530520f-eb8e-3b96-9751-6a5df04c9d92 | -13.2031 | -45.2834 | 2025-08-29 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ac6a6c4d-803b-3d70-91a9-fa8adaa90f77 | -6.9867 | -59.3354 | 2025-08-29 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1832be37-e0f2-3a0a-97da-20661c28f99f | -9.9328 | -59.9247 | 2025-08-29 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fd5e3db5-48e3-3290-a677-218e33be2228 | -5.6083 | -44.9811 | 2025-08-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7298d45b-3df3-3c6a-9cf1-5c635a7a7b60 | -6.7074 | -49.4561 | 2025-08-29 02:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e8743888-df59-388b-a9cc-5a74b8c9bd6c | -6.9683 | -59.3362 | 2025-08-29 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e6f3d3a4-2803-3e2a-ab4b-2eeddb6d2383 | -24.1861 | -49.5515 | 2025-08-29 02:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 71.2 |
| da9dece7-dd00-30f4-94e7-80d5dad36057 | -13.1837 | -45.2865 | 2025-08-29 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a905ef9e-7fdb-3f58-a087-01a287cfabd2 | -10.3812 | -57.8245 | 2025-08-29 02:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f05547d3-2440-38f4-9c56-c2fac900e043 | -9.4263 | -47.6384 | 2025-08-29 02:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| fa55cb59-b910-3240-9d2e-cd70c45886db | -9.4433 | -60.5499 | 2025-08-29 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 60e3d7d7-6bf6-3a3f-9ebb-7ed36344c17b | -9.1525 | -65.7874 | 2025-08-29 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| eb9e32d2-9d82-3246-a287-2f9ad8d7e6c9 | -12.0976 | -44.717 | 2025-08-29 02:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c9ab47d8-1a45-3e81-bcf1-533c58956099 | -5.627 | -44.9797 | 2025-08-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3adc43bd-ffac-34b2-b53c-1e95066f93d9 | -3.4254 | -49.0517 | 2025-08-29 02:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a136d3bf-9ac8-308a-9d65-78cd4661029e | -9.462 | -60.549 | 2025-08-29 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a08bc486-f392-3f36-a6ad-a8e833afd1e0 | -12.9961 | -56.9201 | 2025-08-29 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cc0dbb25-bf38-3d8b-8d6a-cea1213aaa7b | -9.773 | -64.2469 | 2025-08-29 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.6 |
| efeceabb-3fb4-3423-bcfd-1de10b77ef94 | -9.7916 | -64.2461 | 2025-08-29 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7478a90e-20ea-3c70-8e60-b386c6704381 | -9.1154 | -65.7886 | 2025-08-29 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 89859b83-b485-307d-9f11-8aefcdfc070b | -9.2178 | -60.8689 | 2025-08-29 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ff9c39dd-8c1e-3e73-9af9-6d87f3e1b155 | -8.1758 | -61.3755 | 2025-08-29 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 95d8c847-d48b-3072-ab53-e8dfdf1d5a07 | -12.822 | -48.1712 | 2025-08-29 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ef6f95f1-ac67-383e-a2fb-f11a12ea89f2 | -9.7728 | -64.2657 | 2025-08-29 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fe9bdc20-b714-30e6-ade8-c558b69243e8 | -10.3626 | -57.8061 | 2025-08-29 02:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6650587f-01c7-34e1-8ab1-ae53724746ef | -5.6268 | -45.0025 | 2025-08-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 26ba207c-7e94-38ec-a5e8-a82d4f0d090a | -6.5546 | -43.9221 | 2025-08-29 02:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 37ec7a50-0b2a-3ec5-a272-0aee80173815 | -9.0969 | -65.7705 | 2025-08-29 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4b825cba-d1e6-35f4-9532-7f5eab319457 | -13.5386 | -46.8775 | 2025-08-29 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e2401318-2ffe-3740-8e60-c79bfe362910 | -9.4432 | -60.5692 | 2025-08-29 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 97fc8b9a-a7f9-3000-8282-b7526d0bc498 | -6.5358 | -43.9237 | 2025-08-29 02:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b78d28b0-bab7-39e5-a002-7e1a14bb07ce | -6.9684 | -59.3169 | 2025-08-29 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| ce7d3304-1914-310f-b7bb-d42deef486db | -9.134 | -65.7694 | 2025-08-29 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e8d70fe2-e8cd-3266-80ca-82047e72383d | -12.4345 | -63.9173 | 2025-08-29 02:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ac00b15c-3843-32a2-8760-80b39ca4d9c5 | -9.1155 | -65.7699 | 2025-08-29 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 2fb1ea02-ce04-314e-bc2f-189b01bd2dc0 | -10.9712 | -46.9042 | 2025-08-29 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3bca01d9-cc6c-3230-8b49-e76a74f68f50 | -5.6081 | -45.0038 | 2025-08-29 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 98f641fd-9c92-34f8-976f-f6ca7e478bbe | -9.4953 | -45.3678 | 2025-08-29 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| c13ef5d7-9c43-3067-8104-b4fe18920656 | -9.9328 | -59.9247 | 2025-08-29 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 13fea418-67af-3bbb-a061-ff9fdc0d7f30 | -5.6081 | -45.0038 | 2025-08-29 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 382a9680-a1b4-3935-bf4a-548ce238e086 | -9.4433 | -60.5499 | 2025-08-29 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 4607c28b-c50d-344a-9182-332f21fd7c3e | -5.6268 | -45.0025 | 2025-08-29 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 222.6 |
| f20f3fe5-e180-3e00-aaf9-dccb7590d56b | -9.1155 | -65.7699 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 583375b9-8df1-32dc-8cc9-8b76ae53f113 | -6.5358 | -43.9237 | 2025-08-29 02:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 9f9c8dfb-2088-3008-ac2a-4f66296fa5e6 | -12.4345 | -63.9173 | 2025-08-29 02:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c2ad06b3-7044-3b71-b4d0-ed83a059861d | -9.7728 | -64.2657 | 2025-08-29 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c8a976d0-6ff8-33c9-87b6-2dc887e679a6 | -9.1339 | -65.788 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b00dfe8c-5906-3372-b0b5-febb2296be08 | -9.1525 | -65.7874 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e7034e1d-abed-3a59-8ae9-b00fce33d3b6 | -10.8608 | -60.7998 | 2025-08-29 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e58cb381-f7f1-34d2-a35d-b9a3a7b05d9b | -12.0976 | -44.717 | 2025-08-29 02:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 80f5dbbb-35e0-3bd6-a18f-e2972448c94e | -13.2031 | -45.2834 | 2025-08-29 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| abd02c07-0f0c-35fd-9ec0-57c5320306fd | -24.164 | -49.5806 | 2025-08-29 02:40:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bf2397bd-f3fd-34cf-87bd-a1f323d97c0c | -5.627 | -44.9797 | 2025-08-29 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a1e08a8b-9d81-36bc-a982-8f838ee8726d | -10.3812 | -57.8245 | 2025-08-29 02:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 04c648db-ff45-310a-a2e7-284354e433eb | -12.9961 | -56.9201 | 2025-08-29 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 425b702d-f989-3d89-bb92-47c58eebd02c | -12.4156 | -63.9183 | 2025-08-29 02:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| f6ed630f-2960-3f73-9820-589a05098298 | -9.4618 | -60.5682 | 2025-08-29 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| eb7394a8-5e2c-3725-8f77-7ec2ad16b487 | -9.134 | -65.7694 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3454cc27-297a-3a4f-be0f-80a396ec109a | -9.1154 | -65.7886 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 65a39625-37d5-3555-bc2d-9da4b6cd8059 | -9.7916 | -64.2461 | 2025-08-29 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b6a53c5f-3655-3945-99a7-c39b29ad689a | -10.3626 | -57.8061 | 2025-08-29 02:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 327bd304-d601-34ef-bb52-9d215da6f526 | -13.5386 | -46.8775 | 2025-08-29 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| aa693b58-7ca7-342f-b9b5-f9c431731034 | -10.3624 | -57.8258 | 2025-08-29 02:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2d66f4bc-2ced-3e17-8e03-deb9d325d2db | -9.4432 | -60.5692 | 2025-08-29 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| a7a0de14-087d-3436-804c-99fa3599e901 | -9.462 | -60.549 | 2025-08-29 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fd1228ba-ed4e-372a-863c-caa985f76d88 | -9.0969 | -65.7705 | 2025-08-29 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1343b5f2-d6b1-3c63-8f8d-4a137dc9f332 | -13.0151 | -56.9184 | 2025-08-29 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 56ac48be-722f-31ec-a321-152f1a89d2a4 | -8.1758 | -61.3755 | 2025-08-29 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| eeb1dc93-02fb-3456-8b33-652a9683fb62 | -13.1837 | -45.2865 | 2025-08-29 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a230dfa4-7c62-36ad-8279-c9dc5c90dbf2 | -9.773 | -64.2469 | 2025-08-29 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 10a91fd7-8f04-3f8c-964a-70d41adeb739 | -6.5546 | -43.9221 | 2025-08-29 02:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a9a0bc7c-daa4-3ac1-af38-016c611bf390 | -24.1861 | -49.5515 | 2025-08-29 02:40:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e4004408-338a-39d4-bbb8-4c4614902e73 | -24.1648 | -49.5569 | 2025-08-29 02:40:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 129.3 |


[Clique aqui para ver as próximas entradas](README20.md)
