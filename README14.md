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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 919ccde8-1aff-3a0d-b9ad-c5b173e64ab0 | -12.0445 | -63.1356 | 2024-10-25 01:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7d0639e6-5e5c-3639-9ae8-70526f9e6435 | -12.0632 | -63.1537 | 2024-10-25 01:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a3c1920a-1e2d-32d9-a3d1-92ba7704b6e4 | -12.0634 | -63.1346 | 2024-10-25 01:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c6eb915f-d5c6-30e4-aa26-2cc99910c40b | -12.3782 | -63.8821 | 2024-10-25 01:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6ed4ed22-6edf-3384-b3c6-245f0d23e967 | -12.3971 | -63.8811 | 2024-10-25 01:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1b809dbb-8949-3e68-8c4d-56b51357e80a | -12.4589 | -63.1895 | 2024-10-25 01:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 91f9cce7-fc06-3f42-a55e-7d235c01dc54 | -12.4591 | -63.1704 | 2024-10-25 01:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 28d75509-7959-3112-b232-355575f2d1ab | -12.478 | -63.1693 | 2024-10-25 01:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c9a17031-e4c3-324e-af53-f82b8fd2b881 | -12.5167 | -63.0521 | 2024-10-25 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 00324fa9-ae17-38ed-8fe2-e559eb3f2b1d | -12.5356 | -63.051 | 2024-10-25 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 947d71dc-cbf0-36bc-a2c6-0af086a088b4 | -13.4959 | -61.6203 | 2024-10-25 01:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b1cb7ef9-7548-366d-ab0d-ceaba335b312 | -17.0184 | -57.5178 | 2024-10-25 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| eada1579-1712-3ddc-881d-0822302f8794 | -17.0381 | -57.5155 | 2024-10-25 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 88016268-30fa-3137-9623-b4a89ac61d9e | -17.039 | -57.454 | 2024-10-25 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| ec47485a-f563-344e-987d-da1fa9a77a6d | -17.0586 | -57.4517 | 2024-10-25 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| b221330f-14e1-37dd-887e-d772d506d819 | -17.059 | -57.4312 | 2024-10-25 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 6e917f72-21b3-3aec-9efd-75852be7aecd | -17.2147 | -57.4949 | 2024-10-25 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 834d7984-2cd8-35b7-9e09-ebbc954713e1 | -17.219 | -57.228 | 2024-10-25 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 035628cc-5eac-3699-a5c8-ec1784f0a554 | -17.2386 | -57.2256 | 2024-10-25 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| fb9e3e9c-2d23-3692-9d50-2e01904eb844 | -17.8239 | -57.5043 | 2024-10-25 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 22ba7ff2-c738-3935-a673-9f01583f8211 | -17.8042 | -57.5067 | 2024-10-25 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| ffd0246c-bb40-3e18-8975-79bc8e3b70b1 | -17.7453 | -57.4933 | 2024-10-25 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 6174764e-5f8d-3c75-913d-061baa6a2ffa | -17.7671 | -57.3673 | 2024-10-25 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| b007ad18-2756-3df7-af47-34e21192ea3f | -17.9268 | -57.2447 | 2024-10-25 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 6f65f957-4e93-330c-9558-48abf7bbafaf | -17.9272 | -57.224 | 2024-10-25 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| fb664fee-7544-3fc8-965f-5d3063881049 | -17.9275 | -57.2034 | 2024-10-25 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 100747e4-7322-3685-9e51-c91a9ec895d8 | -17.9473 | -57.2009 | 2024-10-25 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| f4844b47-63a7-3d42-9522-2f1fdf08b40c | -18.0431 | -57.3745 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 8ba14a8a-b681-3318-8b4e-8a124a7b0131 | -18.0434 | -57.3539 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| f8d5f42a-f9c1-3999-baa2-2a8ee3b9ffc0 | -18.0438 | -57.3332 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 08dfbcbd-c743-38fd-ad8d-f7fbc8c9ec47 | -18.0441 | -57.3126 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.2 |
| f5b31252-1655-3ae4-bd60-021f41297c6d | -18.0639 | -57.3101 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 862ce744-897e-39d4-bd7b-08626e788315 | -18.0844 | -57.2663 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 6dd8c2ae-8b6e-3fc7-86da-d56e06423cd6 | -18.0847 | -57.2456 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 84570cf5-f917-31b6-b253-0254f6a6bc3c | -18.1042 | -57.2638 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 9f343301-6786-3540-a44e-28d7130aa106 | -18.1223 | -57.3647 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 3ccb48f3-30b2-369a-b3c0-b9497294c385 | -18.1226 | -57.344 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 757b27da-2bb9-3f6f-a4df-c8a63464a81c | -18.1421 | -57.3622 | 2024-10-25 01:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 9c16e500-28aa-39b4-9b08-f396c3a53db6 | -18.3199 | -56.2404 | 2024-10-25 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| e066b86f-cda6-3fef-bcb5-26b592824e63 | -18.3203 | -56.2195 | 2024-10-25 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 5a83ed0c-f72c-381b-b010-90c1ada5f00d | -18.3401 | -56.2168 | 2024-10-25 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| a4fc263e-964e-3bb0-8a61-4ebbe6b623e8 | -18.3405 | -56.1959 | 2024-10-25 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| d007cfab-482f-3429-a3a3-292bb30bd0d6 | -19.6461 | -56.7261 | 2024-10-25 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 9d156a96-d666-35e9-8069-06babc42385b | -19.6465 | -56.7051 | 2024-10-25 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 94ba8628-d53d-35a6-a258-3d847c0a97aa | -19.7266 | -56.7147 | 2024-10-25 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| bf51e00e-6381-33e9-8b4c-426a786b3cf6 | -1.0445 | -47.6237 | 2024-10-25 01:55:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 9a7ea6d3-e100-3423-b10e-55171abda57f | -1.0446 | -47.602 | 2024-10-25 01:55:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1a21e009-44c0-3e06-8caa-b7e829069551 | -1.063 | -47.6235 | 2024-10-25 01:55:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b97c00f2-4de5-3b64-b4f4-b42e2f3dafc7 | -1.1834 | -53.6569 | 2024-10-25 01:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1fb67a9a-c2da-3ec1-99da-22a421a1555a | -1.1925 | -47.6002 | 2024-10-25 01:55:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 609f6b60-b0c5-38b8-aa0a-921c4755b4cd | -1.211 | -47.5999 | 2024-10-25 01:55:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c34edb93-d5f0-312f-a995-735c28bf655f | -2.6193 | -52.4359 | 2024-10-25 01:55:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 13ac10b9-ffc7-33ec-ace1-fb9d75e361e1 | -2.6482 | -49.2465 | 2024-10-25 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f866c347-bb51-3eeb-afce-0e186a58db61 | -2.796 | -49.2424 | 2024-10-25 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f1714dea-8aff-314b-8972-25b6ba99f440 | -2.8144 | -49.2631 | 2024-10-25 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4a11ba15-b3dd-3297-8384-6b8aab433e4b | -2.8145 | -49.2418 | 2024-10-25 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| dad0c40a-676b-3d25-9478-037db7a2a8d6 | -2.9578 | -50.4198 | 2024-10-25 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 17dd4b76-a55c-35a0-ad29-3a0eac1edafb | -3.2135 | -46.8063 | 2024-10-25 01:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 88561dea-d559-3585-a740-bb957ce928bf | -3.2136 | -46.7843 | 2024-10-25 01:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| da3fb145-53ec-37ff-af0d-555597e287ce | -3.9396 | -46.4229 | 2024-10-25 01:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c5ec944d-3fcd-3e06-a012-e2df58d04585 | -3.9581 | -46.422 | 2024-10-25 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0b47206d-2f44-3bdb-b801-d7f49a1df04b | -4.2429 | -48.5474 | 2024-10-25 01:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| c814cf6b-adff-3b84-8d99-007fac4b9672 | -4.5045 | -48.2117 | 2024-10-25 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 96ac42aa-f25f-36e6-9934-89a4db3513ed | -4.58 | -48.0132 | 2024-10-25 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 339e8411-b69d-38d6-a4f9-8e6c0712ab06 | -4.5986 | -48.0123 | 2024-10-25 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6a90fc16-cbd4-3b24-abd5-a77e2269eb69 | -5.9788 | -45.3621 | 2024-10-25 01:55:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 57d552f6-c59a-3ac5-8bfc-a50a24c2485b | -6.5219 | -60.0457 | 2024-10-25 01:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 2ac79cfb-89ee-3502-a147-cf08099c4f63 | -6.522 | -60.0266 | 2024-10-25 01:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f252adc1-15fa-3e6c-abc1-d2913612a22a | -8.9064 | -48.544 | 2024-10-25 01:55:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 27a87e1a-f894-3ade-b365-6619cfcf0d52 | -11.902 | -56.4135 | 2024-10-25 01:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1d66f1b9-fe72-3878-901a-b6a95f6e1fbc | -11.9822 | -63.9213 | 2024-10-25 01:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bf9f6699-a0f9-3411-be3b-6f40075acd14 | -11.9824 | -63.9022 | 2024-10-25 01:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.0 |
| bd6e69e9-7905-3133-8184-33c246c18e55 | -12.0011 | -63.9203 | 2024-10-25 01:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6181f334-e782-3fe3-8e14-b0e3f06cdc32 | -12.0012 | -63.9013 | 2024-10-25 01:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 81c475eb-f472-3e85-8894-991f21a61231 | -12.0444 | -63.1547 | 2024-10-25 01:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e826831e-bc03-306a-8abf-cf88bcf9e423 | -12.0445 | -63.1356 | 2024-10-25 01:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1b9a4f63-1385-37fb-9774-366749e4e6bd | -12.0632 | -63.1537 | 2024-10-25 01:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 12959c1a-1357-3061-928d-38360a3c21ac | -12.0634 | -63.1346 | 2024-10-25 01:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 269cb1d8-635a-338e-a04a-2017b2d8a074 | -12.3782 | -63.8821 | 2024-10-25 01:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| fd9a243f-7c2a-33c3-a3c7-510149968896 | -12.4589 | -63.1895 | 2024-10-25 01:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5cb44dc7-8e9b-3b5c-9dce-4003b3e6d6cf | -12.4591 | -63.1704 | 2024-10-25 01:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3ca188fd-9950-37c0-a472-0b4b5fd523eb | -12.478 | -63.1693 | 2024-10-25 01:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ff957b14-9b53-3555-838b-62af1f175ba1 | -12.5167 | -63.0521 | 2024-10-25 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 22bbed8d-d82b-3acc-8239-1f0c81b064cf | -12.5356 | -63.051 | 2024-10-25 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4221d9f5-872e-39f0-9aab-0ae6736e03cc | -16.9596 | -57.5245 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| d1eaf7b8-efd1-3caf-abf5-ca05213a96e8 | -16.9789 | -57.5428 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 6d128bae-573d-3558-b776-1663f11103e8 | -16.9792 | -57.5223 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.9 |
| a738524c-6717-3816-9718-cc4920d8c8ef | -17.0184 | -57.5178 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 68a0de0e-ed49-3663-93a9-f252b3be6a6c | -17.0381 | -57.5155 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 3f9b021b-79d3-3790-941c-6c5dcff9f4c9 | -17.039 | -57.454 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 2e53b10b-84ec-3f43-93ac-69ad59f7e346 | -17.0583 | -57.4722 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 39932c7e-00c7-34b7-8b0f-3e09c25fc8f3 | -17.0586 | -57.4517 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 345c787a-a966-34fe-b16b-37d5262adbe6 | -17.059 | -57.4312 | 2024-10-25 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| aa6bda96-755b-3a03-b9c0-59cfe4c55e11 | -17.2537 | -57.5108 | 2024-10-25 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 9e618106-7af1-30bf-bfea-46a294d55ff8 | -17.7453 | -57.4933 | 2024-10-25 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| e1979dd4-480d-356b-83d1-1e1073ec7bf3 | -17.7671 | -57.3673 | 2024-10-25 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 38246291-e6bb-3230-91e8-7508b62011e0 | -17.8042 | -57.5067 | 2024-10-25 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 067150fa-125f-3dc5-b1a6-49633623a64f | -17.8239 | -57.5043 | 2024-10-25 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 909c2e25-7ab5-3b61-bbd7-c375f2018cfb | -17.9268 | -57.2447 | 2024-10-25 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| e23c5016-4609-32ea-8a1b-3ba45e3f0953 | -17.9272 | -57.224 | 2024-10-25 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |


[Clique aqui para ver as próximas entradas](README15.md)
