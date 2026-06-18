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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08354fad-e076-35c7-9702-38df9111e9e4 | -9.94185 | -65.01485 | 2026-06-18 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e3dd6b8-262f-3698-8ccc-bb0062e773a8 | -10.70969 | -49.66879 | 2026-06-18 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87330061-1d03-32d0-9c10-7ceb8efb8415 | -10.151 | -56.61135 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b598d2c-68d5-32d1-ac11-2bb1eb991d76 | -10.78388 | -53.57939 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51b3976e-b6c5-3c8a-aca1-d028280929ff | -9.21123 | -47.92894 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90472281-f754-3a6c-ad60-85d07dadc862 | -11.26212 | -53.95993 | 2026-06-18 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd00b8c5-91a9-328b-a9a5-6beb706df24d | -10.56048 | -46.22908 | 2026-06-18 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b069dec-eea2-35c6-8514-307c958d84f0 | -18.82834 | -51.47326 | 2026-06-18 05:23:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 991e6f21-6179-35f3-9b40-0e9393697308 | -10.15786 | -56.6124 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de11a49a-b88a-3084-a17b-54727223279e | -9.21657 | -47.9346 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac7339a9-3099-3322-8cd5-8f2644dd30a2 | -11.24898 | -46.6248 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b68a8db9-5705-3cb1-9d2e-3e475c7122ae | -13.19845 | -50.33878 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bf68f44-ca9f-3cfa-abe1-f156fc2b353d | -14.09571 | -59.46333 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37bbe11b-6eb9-38e8-9689-dde02af30acf | -10.58259 | -53.48203 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5caa066-a718-3910-ae33-e668f9568652 | -13.20364 | -50.33956 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62e8ac64-da6c-3149-aceb-e3712e566eb1 | -11.24766 | -46.63741 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e00facc-349e-32c3-a328-28af96d71169 | -10.55955 | -46.22924 | 2026-06-18 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c5971b3-3c42-376d-b9b0-1a2e0a1f6b13 | -10.91569 | -56.85726 | 2026-06-18 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d870851-db93-3e64-9c76-b1c2ebe496fa | -9.21712 | -47.93051 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d75a3817-c846-3dfa-9e71-728c41c3534f | -10.15729 | -56.61615 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09593674-cbf7-338a-a510-96e82eb6815a | -10.91227 | -56.85673 | 2026-06-18 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d9bab5b-2416-3f9e-a8e0-3b6653cfbf42 | -10.54569 | -53.71868 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7120cd4-e64d-318c-a367-f37d3d9180f5 | -10.98615 | -47.75108 | 2026-06-18 05:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe508129-67c2-3b5b-8c87-c24645b9e1db | -11.79752 | -57.35558 | 2026-06-18 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f1b43b0-b493-3624-b577-02e5829b341f | -11.66455 | -56.76442 | 2026-06-18 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc2caad-f30a-31b2-9fb5-598ae0273505 | -9.7483 | -47.87599 | 2026-06-18 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceba7e04-2efb-3ec7-9b60-1d342a5128f7 | -11.80626 | -52.52368 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc7b00af-808e-36e5-916c-cc19c42b95bf | -16.17861 | -59.33601 | 2026-06-18 05:25:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40704df8-9fcc-36cc-8fad-4f324adc3561 | -15.64914 | -58.01648 | 2026-06-18 05:25:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2df0cab8-137c-3ae0-b58c-3d05d017eecc | -15.86316 | -58.3536 | 2026-06-18 05:25:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fe03d5c-44c7-36b3-95b0-10a4af11a8bf | -12.8354 | -44.3657 | 2026-06-18 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 61aee1fc-b92f-3070-83f7-b7b3684df605 | 0.8943 | -59.69042 | 2026-06-18 05:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a917ffe-a94e-3710-8c2d-db4a9ce3fb44 | -3.85027 | -54.22092 | 2026-06-18 05:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9081c257-fa10-3ec5-ae5e-3c2fe34ef7be | 2.58886 | -60.69325 | 2026-06-18 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f14ba79c-091c-3da9-8c41-c064c24e28e4 | -2.73765 | -58.19553 | 2026-06-18 05:38:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 78db950a-5ecb-3ee7-b815-367a43603f9c | -2.73844 | -58.19047 | 2026-06-18 05:38:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d519029e-352d-32de-a2b1-8859fee3dd4b | -3.84979 | -54.22418 | 2026-06-18 05:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45b1e1df-fd08-393b-8c38-8ef0efd74fa0 | -12.8354 | -44.3657 | 2026-06-18 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4bfa543c-f82c-3ca4-8895-79547b99064b | -12.20908 | -52.78236 | 2026-06-18 05:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 179143e3-0797-3e14-85e8-2a2e35cb62f6 | -9.93796 | -65.01488 | 2026-06-18 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba59f5cb-db40-345f-a7ee-75a4a733f527 | -12.20893 | -52.78336 | 2026-06-18 05:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e36c427-c7b0-3ff0-bab7-79bcf9756c67 | -11.26344 | -53.95615 | 2026-06-18 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2742ba96-8518-3afd-8984-d50418a20337 | -9.94127 | -65.01543 | 2026-06-18 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b86802b-d674-3419-9e6c-5a3cad124784 | -9.94239 | -65.00843 | 2026-06-18 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 547754bc-7b25-3b0f-95fb-251c9f494134 | -12.24458 | -56.1745 | 2026-06-18 05:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1ec053d-df8e-3003-8780-d781f4386f92 | -10.77214 | -54.10992 | 2026-06-18 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7d079c2-129d-39fd-8b0c-dbcb370f68cb | -10.91398 | -56.85796 | 2026-06-18 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7ee20d77-30ab-3f33-bc9b-8835ac2f7cba | -10.59366 | -53.51733 | 2026-06-18 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edcc7bae-baa6-3ce5-828a-67d1df252d23 | -12.20307 | -52.77693 | 2026-06-18 05:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f6664d8-a7ca-3b14-9c3c-95e9955203dd | -9.94183 | -65.01192 | 2026-06-18 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c148938-718a-3264-9d1c-272591cdb46f | -10.2787 | -60.54086 | 2026-06-18 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac6bae7c-1ee4-3759-9d86-4506867e3f97 | -12.20955 | -52.77782 | 2026-06-18 05:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec89d1c4-09b2-3031-9f7f-2003da1b06d4 | -10.90983 | -56.85172 | 2026-06-18 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2aab2c6-1522-3b28-91d7-b279c42df128 | -10.91473 | -56.85234 | 2026-06-18 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e71f60be-b997-304e-b0e7-3538bb4f66eb | -10.77265 | -54.10569 | 2026-06-18 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a67fa4c-5023-3e9a-9797-3cbd9ebaed21 | -12.20325 | -52.77595 | 2026-06-18 05:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1a74491-8272-3fcf-8e99-e25c03418e9b | -10.59309 | -53.5219 | 2026-06-18 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef9ff310-9714-3f21-9b26-10df54a347ed | -10.59424 | -53.5127 | 2026-06-18 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d1aa47d-4b0e-3924-ac1e-3a87b8f8d365 | -13.65246 | -60.62092 | 2026-06-18 05:42:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdecd078-fac5-38b3-89ba-4ae4b5aad1e9 | -14.09174 | -59.46944 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34c3cd4f-18b3-3da2-acb4-ca1fc917dd96 | -14.09283 | -59.46124 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 942ef329-8548-3ef8-8d51-df9e9e703b6f | -14.09658 | -59.46589 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9b82c43-15aa-32c0-bfff-d7c37f0937ad | -14.09228 | -59.46535 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acf68926-840a-3fcc-8e00-66d7000c68b2 | -15.64639 | -58.01915 | 2026-06-18 05:42:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22420ccb-4c48-36dc-92cf-a3ecb77db8c5 | -14.08961 | -59.4525 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ac31332-6eba-308e-afef-a642b9fe9c5a | -14.08853 | -59.4607 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 891ae44e-6430-33e3-a900-5131e849b8c2 | -14.08907 | -59.4566 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 114b0218-7b9b-32c2-9632-53d4031eaec1 | -15.64709 | -58.01335 | 2026-06-18 05:42:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd2b4218-8a0b-3ab2-80f2-7587d8d6d6fa | -14.09337 | -59.45715 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09ac72f1-b7cd-32ef-9607-2ab4997c23c5 | -14.09712 | -59.4618 | 2026-06-18 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32b161f0-231a-3a63-9189-490cbb8c4248 | -18.98999 | -52.45792 | 2026-06-18 05:42:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af293e32-3e94-372e-bdbf-23e0ac8f9c2a | -12.8309 | -44.36769 | 2026-06-18 05:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4e9106b9-abf8-34fe-9994-842c728dc30b | -12.76243 | -44.53869 | 2026-06-18 05:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 13d8ce24-47b9-3b7a-8998-6291adaab4f9 | -12.8354 | -44.3657 | 2026-06-18 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| ea28548a-c8a3-38b6-bcf5-d80cb0621f4c | -12.8548 | -44.3625 | 2026-06-18 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 51cc689e-349a-3444-96aa-e8a37c4a31b9 | -8.9072 | -46.9621 | 2026-06-18 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0634ca3c-b198-3580-b367-58eda8daf6c0 | -16.02242 | -43.42257 | 2026-06-18 05:50:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 63ea3253-79a3-31f5-b7c7-6adcff438481 | -17.31207 | -43.64277 | 2026-06-18 05:50:00 | AQUA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 27cbaf44-4285-3817-ab90-7f5eeb3c7776 | -12.8354 | -44.3657 | 2026-06-18 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7962a9e3-ef67-30cc-b014-2268a265f295 | -12.8354 | -44.3657 | 2026-06-18 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| cfec8feb-3eb2-3237-bec4-264235d76bff | -8.9072 | -46.9621 | 2026-06-18 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 68ba1942-a2a9-3268-8487-f5546926bbe5 | -8.9258 | -46.9824 | 2026-06-18 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 02118a6e-bd80-304a-9117-93f30b56e9a5 | -8.9261 | -46.9602 | 2026-06-18 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 458ff81f-a1d5-3857-8c11-78e740441ae0 | -12.8354 | -44.3657 | 2026-06-18 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a7706232-f497-3c61-8a06-23b1c712dbe7 | -8.9069 | -46.9843 | 2026-06-18 06:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8c5a79e7-638b-33b7-97fe-482cc3ae0cf5 | -8.9072 | -46.9621 | 2026-06-18 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6274c953-f648-30dd-a63f-e7f08d900bb7 | -8.9261 | -46.9602 | 2026-06-18 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| f8b0d93f-ebb1-368a-81c8-e1fd55cb0b7e | -12.8354 | -44.3657 | 2026-06-18 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3657f392-322d-36be-8159-4f7e54c599e6 | -12.8354 | -44.3657 | 2026-06-18 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ba91de89-141d-3e05-bbf2-e2f5c42ca4f7 | -12.8354 | -44.3657 | 2026-06-18 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 06e4f1db-3c5c-39d1-a8b3-faf0b29085ac | -12.8354 | -44.3657 | 2026-06-18 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 0d361f4b-404d-35a5-ae25-f05f40bf7fae | -8.9261 | -46.9602 | 2026-06-18 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5c1f3e00-9657-3c78-988c-bcffc35551ba | -8.9072 | -46.9621 | 2026-06-18 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3cc7e319-c035-3405-b159-4a13bbfc5475 | -12.8354 | -44.3657 | 2026-06-18 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 79bb8c5e-1b32-3357-8284-f3bb0e572229 | -8.9261 | -46.9602 | 2026-06-18 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ee2861e5-9769-3644-8799-51aa196a1e0c | -12.8354 | -44.3657 | 2026-06-18 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 97155cd5-d5bf-3e89-9a51-32ce4ecb6736 | -10.9219 | -46.4162 | 2026-06-18 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 751a2f90-125b-3ee4-855f-f45fb6597370 | -10.15078 | -56.61745 | 2026-06-18 07:26:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd76e9e2-2d57-3755-9364-3435007237d1 | -10.90914 | -56.85752 | 2026-06-18 07:26:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| dc3c3fc6-59fa-3a7b-9af2-db24e3180e54 | -14.09074 | -59.45486 | 2026-06-18 07:26:00 | AQUA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |


[Clique aqui para ver as próximas entradas](README14.md)
