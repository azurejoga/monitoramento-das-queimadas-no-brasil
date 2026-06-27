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
| 8e22d026-b560-3547-a8da-9311267d044c | -22.97068 | -52.69644 | 2026-06-27 04:34:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 732832c5-44ea-3473-8e96-71a56536ef07 | -18.4618 | -47.25216 | 2026-06-27 04:34:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea2cc214-688c-3d82-a2c7-0142f1ce9290 | -16.75241 | -45.81483 | 2026-06-27 04:34:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95e32f21-8fc5-3011-a316-0bc320056a35 | -21.77347 | -56.28283 | 2026-06-27 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73235dd8-d927-3ae4-81f0-d5663b6d51ce | -18.81556 | -50.96651 | 2026-06-27 04:34:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c306a2b-e47b-383f-bcb1-b0a1633a861e | -17.83904 | -50.9663 | 2026-06-27 04:34:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d30a6edc-7cfd-3b4c-9018-65208ce43471 | -21.77266 | -56.28701 | 2026-06-27 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53f0e1f4-fd2d-3ded-b400-ea1b86aa1e93 | -16.57855 | -49.53376 | 2026-06-27 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 011c1a90-ee64-31ed-8cb7-b05977a5df39 | -16.94862 | -53.60373 | 2026-06-27 04:34:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef84bab-3b2f-3ba1-9d49-100edf4316d3 | -16.52608 | -47.73662 | 2026-06-27 04:34:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ff6562f8-5efd-3ba2-bc2c-49237ffcde37 | -21.77768 | -56.28387 | 2026-06-27 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e5d1906-da21-3ea1-b0f0-e2cdb9bbdfd4 | -21.29152 | -56.87514 | 2026-06-27 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cfb58e9-352a-31f0-acf6-f38a1073d810 | -21.77687 | -56.28802 | 2026-06-27 04:34:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c375d9f5-45cb-30b9-9add-263eb457a09f | -27.45533 | -48.45036 | 2026-06-27 04:36:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 535b47e7-58bc-3e08-a41e-59316c1b2f3c | -27.63846 | -52.13338 | 2026-06-27 04:36:00 | NOAA-20 | GAURAMA | RIO GRANDE DO SUL | Brasil | 4308706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a306e21a-b931-3913-bfa5-d7e1cb56c953 | -27.67741 | -49.69466 | 2026-06-27 04:36:00 | NOAA-20 | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9bc95257-b35a-3fad-bca2-7da584d5a4bf | -27.64178 | -52.13406 | 2026-06-27 04:36:00 | NOAA-20 | GAURAMA | RIO GRANDE DO SUL | Brasil | 4308706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1c76e79b-0e27-356b-b70d-be1a780eacc1 | -10.6195 | -50.2038 | 2026-06-27 04:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 5f08d99b-9b60-3443-85ea-5d2ea5b2c125 | -12.6236 | -57.8926 | 2026-06-27 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1bce4b87-d99a-3c03-b456-5c4aa61aed5b | -12.4651 | -58.5009 | 2026-06-27 04:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 35355133-db41-314c-bd14-e932c561da7e | -12.4654 | -58.481 | 2026-06-27 04:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 32c76954-8561-3a60-adfe-1d09b6fd59c5 | -12.6046 | -57.8942 | 2026-06-27 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ff0017ec-e1be-30fc-b8b9-d83fddbd7a95 | -12.6046 | -57.8942 | 2026-06-27 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d79a592d-547c-3d17-8e59-6b9c3b906396 | -12.4654 | -58.481 | 2026-06-27 04:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c2e00663-ddbb-3c12-a2fa-33d798871640 | -12.6236 | -57.8926 | 2026-06-27 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ae44e5c5-221d-3267-bd7e-6fa7a4cffadb | -12.4651 | -58.5009 | 2026-06-27 04:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f731e30a-f34d-3310-bd89-c45a80e6e8ed | -12.6236 | -57.8926 | 2026-06-27 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ed62ba1b-7199-3bcb-98e9-38307df65d3c | -12.4654 | -58.481 | 2026-06-27 05:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| dcf51037-4a4c-34b1-878e-c3a5c22c1ba2 | -12.6046 | -57.8942 | 2026-06-27 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 57c3e0df-9ee1-325e-98f5-77afdd3d567c | -12.4651 | -58.5009 | 2026-06-27 05:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b5234d4d-b001-3d3e-8e8a-66d9439dcd02 | -12.6236 | -57.8926 | 2026-06-27 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3fbed5fc-de02-3a92-a746-72473afc2161 | -12.6046 | -57.8942 | 2026-06-27 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 97aa0b3b-049a-301f-a4d6-af6cb25b8839 | -12.4651 | -58.5009 | 2026-06-27 05:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d57bf298-d2a6-3745-a48e-a211a2256d9e | -12.4654 | -58.481 | 2026-06-27 05:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9dc8846c-69ed-36cb-af85-51a2d2b2d2c9 | -3.73062 | -53.78457 | 2026-06-27 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c901a101-45a1-3fcd-9d5e-351dd63fc664 | -7.62747 | -47.30014 | 2026-06-27 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9986f44-34e9-3b33-9dc4-c1d62f26fa56 | -3.73194 | -53.78625 | 2026-06-27 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2f5e521-6444-34c9-95d4-cca643171412 | -5.77378 | -45.07209 | 2026-06-27 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4acdfd7b-f5e4-3b33-a7c5-b3452bfcbdcb | -4.28475 | -48.35922 | 2026-06-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fd13564f-f898-367e-8fa4-bd1e36bf85ef | -7.63054 | -47.30128 | 2026-06-27 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a9cd62-27a4-3b44-8aa6-b90c0f557691 | -4.28419 | -48.36311 | 2026-06-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d615b746-abec-3961-925f-e0c13c0f0fd7 | -4.28366 | -48.36674 | 2026-06-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 572cbbec-18e0-3ab5-854c-19792145e0e3 | -5.78169 | -45.06666 | 2026-06-27 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b6fe243-d8d3-3d62-9d6a-be76381154b9 | -7.62424 | -47.30021 | 2026-06-27 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b3814ab-35fa-303a-ac76-23a4b79c3842 | -5.77468 | -45.0653 | 2026-06-27 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 18c8935a-7b40-351f-97c2-a208936f1679 | -2.32595 | -60.0597 | 2026-06-27 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5f80241-b2e4-37ab-a8db-73630c03049f | -9.03311 | -61.33726 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3260630-f62d-3bfb-9783-c972018fae05 | -11.04867 | -52.46392 | 2026-06-27 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79dde60e-afa6-3aa5-993b-b84f2ae82d9d | -10.93787 | -56.85897 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca184b5b-9a4f-3cd3-b17c-787fd9117141 | -12.62728 | -57.89518 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 312438b2-6480-354e-81b2-c973629befe4 | -12.62324 | -57.89854 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44612a11-2a97-39b0-acb9-dd3d79c168a2 | -10.47958 | -47.11436 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f6d30f6-f7dd-3057-8b90-1a10c0f24ed7 | -10.4763 | -47.08466 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3a32573b-70b2-3a84-922b-b9a84cf1c044 | -10.55777 | -46.25077 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0886f906-1b0f-39f7-a258-c78da5f46709 | -12.51963 | -48.28942 | 2026-06-27 05:18:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08375b07-a28c-3e7f-a1ff-489ed658e410 | -9.47504 | -48.06612 | 2026-06-27 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ebc5e67-009c-3c7b-90bd-9e4e72e8a25d | -10.30702 | -57.14039 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bcacc53d-4a88-3c00-9217-f7dac6fc2594 | -11.79612 | -57.34762 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 335a8005-f878-349c-b728-83a9c17f64cf | -9.02539 | -59.54171 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4220f147-800d-3e8f-a5d4-9c0b210011a2 | -11.87521 | -57.81721 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2797025e-04dc-3fb0-8ef0-3f1f48e1592c | -10.54468 | -53.71522 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5266d519-4abc-347f-a5a6-9ec23c1afbff | -12.16931 | -59.75631 | 2026-06-27 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e5e3e63f-598f-3f08-945c-d0f30981f4ed | -10.90871 | -56.85896 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653740e3-1865-33a7-b056-d814b1332ade | -10.49753 | -47.13329 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb6d8670-75b5-3132-b8e9-819e158c8a86 | -10.18967 | -48.50273 | 2026-06-27 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07044670-5f26-3242-a3c7-38f49b8f8dcd | -9.59311 | -56.92515 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d5af3c08-8468-325d-b768-7106e289b6a3 | -11.65166 | -54.89269 | 2026-06-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9abffff0-ee72-3e60-9dd8-f81b8cceabce | -10.3829 | -56.71902 | 2026-06-27 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72f90df2-1a8b-3ca3-8acb-55035bdae0e7 | -12.36635 | -57.73319 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e9c65a-b98f-3836-af77-3a86cbbd019a | -12.45443 | -58.49121 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f8cf92bb-5f19-38e8-b6af-63c044331007 | -11.79202 | -57.35112 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84bcec22-28f8-304b-a600-8d572c0d69d2 | -9.03371 | -61.33353 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b37a9f1e-2f32-3c99-b000-5dc0289935f2 | -10.72322 | -56.22739 | 2026-06-27 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2653792-aa0f-3ea3-bcc8-0652978b5da4 | -11.66102 | -57.25529 | 2026-06-27 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df361ae7-b419-3821-a8dc-87c6f8658660 | -11.66454 | -57.25584 | 2026-06-27 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6673147a-dd6d-351c-a9ed-68432b28d0b1 | -10.93907 | -56.85081 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c58e566b-420a-340a-9e4c-5d3dbc377bee | -12.22228 | -56.56107 | 2026-06-27 05:18:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58b04035-c376-309d-b506-1f46928fd537 | -10.56612 | -46.23953 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73bf50f1-ec59-39ea-bce1-1d649ce65106 | -11.9102 | -57.40891 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 52d87f11-4569-3b7a-9d84-92d639622453 | -12.61109 | -57.88475 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| aa51d568-cf1e-30c0-b6bf-bffc2078b132 | -12.61688 | -57.89362 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1a1a5223-128d-3fbf-993b-920dd1b7f47c | -10.77807 | -46.47345 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aff860c-b5c5-3fc9-88fe-a747fa6cab7e | -12.46121 | -58.49226 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| fd192dc6-a94e-30c2-a183-7c2d408a4ec7 | -11.32261 | -54.47116 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2418cef-a6ec-3af4-b8ab-8d4f8f939744 | -9.59253 | -56.9291 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aac9e041-1705-3aef-acff-b5cfbd617268 | -10.39418 | -56.76661 | 2026-06-27 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a07c897f-869e-3c2a-bb33-492df9ba556f | -11.51546 | -56.12939 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 814d3699-0be4-3331-9ccb-d3ebd62730d0 | -12.36798 | -57.73461 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d976572d-2b6b-32ec-9349-471a1396fc45 | -12.45782 | -58.49173 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a881a06c-ecf1-36f0-967b-177385f2d249 | -10.49036 | -47.07973 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8202b220-bf42-3f29-b400-9d2779e211b8 | -9.03491 | -61.32608 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9a3734-56ba-3d5a-a5f9-9ddd6b94ec5a | -11.32312 | -54.46735 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f14329e-8a9d-309d-bf8d-0eccb008691a | -11.51305 | -56.11969 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb22d9e-0915-3516-badc-46ed482b433a | -12.43535 | -49.57912 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ade82633-602a-3ac5-ac67-b09355107ee7 | -10.54742 | -53.71478 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d93f5353-b0d3-3331-bf49-bc719ead39f9 | -12.61977 | -57.89803 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bc14202-2c71-3385-93bb-69525e6237ee | -10.79282 | -56.75836 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ed76863-be2e-3279-83ec-14943687fbc7 | -12.61341 | -57.89308 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9cb0170f-54ea-35ef-a651-ca67757b5309 | -11.87464 | -57.82108 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8f44934-f18b-38a8-8dfc-06040c9b096c | -12.45261 | -49.58235 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
