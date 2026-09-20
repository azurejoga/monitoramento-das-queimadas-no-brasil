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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c6d8c85-5082-3bfe-917b-b72884622474 | -11.84776 | -46.87341 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e81f4368-0f8c-3d8b-a7e2-dbf7c8f5b89b | -11.85339 | -47.67985 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 48d12aa6-aca4-35f1-9490-f34d229a294e | -7.55781 | -45.44081 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e96c5fe0-8032-3395-bfaf-aa5cfeb49a9f | -11.47465 | -45.34295 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131a1e9c-5f18-38c4-926e-6c6734a75c92 | -7.4234 | -44.70232 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3947870f-fff0-345b-9408-acb3191b876b | -7.7672 | -44.83742 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d032edb-8d1f-3557-b3d6-c5a2e2acd7ed | -7.49611 | -46.70935 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 253bef31-eab5-326b-af0a-15d1bb2676f5 | -10.41745 | -48.32747 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce839118-9403-3ed2-89e2-e3ba2c1b340a | -10.3855 | -48.99369 | 2026-09-20 03:45:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9eb20d24-c982-3553-a10c-e76f57e88fac | -6.99441 | -45.67669 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a8fde52-3fd8-35af-a270-9b2e86c8a413 | -13.22423 | -46.9435 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 035ede4c-da2d-3d4f-9c55-a0120ae03287 | -12.13759 | -47.03683 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 286c5ea5-98e1-322a-bc95-b276b18bf404 | -7.28187 | -45.55272 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2033e3cd-ab70-3064-aa0c-50195a67970d | -7.36008 | -44.87088 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e8a89741-da03-3d10-a612-109cbfb87b1c | -7.88148 | -44.86465 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f65af124-c625-3a8d-ae12-51520085ff9b | -7.9702 | -44.06493 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b21aca5c-15b7-319d-a4c0-08fc03778717 | -9.79198 | -45.06771 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 664a56a5-26d2-30e5-9e31-05c9cdea4746 | -6.18316 | -47.49549 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b4b589cf-2d67-3a76-9e27-83faaa4c18f6 | -9.1203 | -45.72612 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc50738e-c43b-3882-a8c9-2c87222f52c6 | -7.42624 | -44.74749 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f3647d3-a4fe-3784-be22-6155941de2a9 | -7.02822 | -45.25673 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb3a196f-f5f6-3ffb-bc2b-2c1bd91c3048 | -11.85419 | -46.8703 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3803a05f-8f45-390e-8bee-f798c2226205 | -7.43573 | -44.75559 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4849e4f0-9349-3d5f-97d7-2f9a9b11c72a | -10.92937 | -48.31282 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64ffb8e5-a00f-37a4-a29a-67a1396f5fd2 | -10.7776 | -46.32833 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5745c318-ccab-3fec-9f96-93a0c74e45e7 | -10.56146 | -46.56939 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f339747-dba3-383d-a502-4bfae4cab57c | -11.45324 | -45.71846 | 2026-09-20 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 450e8502-340c-31b7-87e9-3d3924d7378a | -9.12648 | -45.72335 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4962229d-e6fe-3059-9348-cf7a9b5d429a | -10.3128 | -50.22722 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 79bb5097-d5f9-3e24-805e-09fde93f0d5a | -11.66416 | -43.42041 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07e76ddd-57cc-3ffe-9681-30b94d30f6be | -9.81135 | -48.32676 | 2026-09-20 03:45:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dec49582-6d02-3259-b9bd-dff08abc5872 | -10.31713 | -50.20639 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 42dcda1f-8ad9-3a4b-a270-477d7e2314d9 | -6.68503 | -43.63156 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e50bb888-746c-328d-8247-44b9028071a3 | -12.99526 | -46.91811 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7284a97-ef75-34ca-87be-bfb89fe3f4ad | -9.26171 | -45.94561 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3388be4b-6e1c-358b-b664-bd965ee58211 | -7.96863 | -44.07373 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85224656-103b-35d5-afcf-d7a4abef2206 | -11.00726 | -48.32025 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f03f000b-0965-3778-a6cd-8e322bf258ca | -6.76075 | -47.92575 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e3a691-3a3a-3cee-8303-157647a91c50 | -11.86283 | -47.66318 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a0e52ce-b812-3225-83c0-8af10253b60f | -8.50487 | -47.44117 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59958a89-71a6-3f80-846d-35bf5dbbf73c | -12.13643 | -47.02959 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ececfa6-0f66-380d-bcb6-7c359f1fe856 | -11.85514 | -47.67101 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3df7992a-f859-3d66-83ec-cfe7fab3795e | -8.78836 | -48.71202 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c8228e00-9803-395b-967f-ba38ea914012 | -9.72996 | -46.09375 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faa63755-15d6-3dad-9617-8162b799519c | -7.77134 | -44.05209 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72c945d4-647d-32fc-a0a3-cf9f0fbec465 | -9.02391 | -48.72363 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce510e5b-1ad8-3d1a-bd61-4a8e654a350a | -13.02947 | -46.91942 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2fb4863e-12b2-320f-a2b0-9e55c0585bc3 | -11.48196 | -47.76067 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f3ff3c-9208-3443-8f43-62df2542d54b | -11.66783 | -43.42583 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95486139-784f-38d0-96d3-766618cb68a9 | -7.02047 | -45.23636 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f040148-b29f-33b9-b6ad-2bb9b03a3400 | -11.08924 | -48.29934 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3f001097-cdd5-30b6-8052-ccbf9ef9d2d8 | -7.59883 | -46.97392 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c06431-d95c-3de3-97ff-4dffb04586f5 | -7.76335 | -49.19913 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5bafc66f-2e23-33bd-8d5a-2d9cb4de0267 | -9.77118 | -45.06393 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42a0cdc2-31a9-345c-a97e-8f99db7b088a | -13.02214 | -46.92406 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3455b5ae-7191-3eec-b27d-51cb483b3e3d | -11.78628 | -49.82933 | 2026-09-20 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4aa05876-7014-3e7c-8a5f-1074099a169d | -7.76663 | -44.84062 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c908b768-b563-38b2-a781-9984eb7389b1 | -10.93371 | -48.31032 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 205f4177-10df-3c03-8a54-1bd5f79a173e | -7.48924 | -46.71293 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20c7b503-5bb5-3914-92e6-321d2e2a633d | -7.548 | -45.43175 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 721d9228-ca8b-3a6a-9008-65ccaee0916b | -7.88206 | -44.86135 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6c0f2c9-e7a6-347e-8721-ab3d3da99981 | -9.45952 | -45.43252 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56dd1048-2fa0-35e4-b35f-c9059721ce57 | -8.50698 | -47.43645 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f30a38fb-b240-32e1-b972-a5691e3dcbee | -10.13592 | -45.55614 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fee78a27-401e-34fd-8360-17114b48e7bb | -8.99711 | -45.00382 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abdcfd2e-7c61-3382-bbda-40ad6e86f80f | -7.54181 | -45.43444 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4af7dcba-5971-314b-be1f-7acefc4baf13 | -8.49955 | -36.27627 | 2026-09-20 03:45:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d15660d-74ca-3c76-aa22-93109d083a19 | -10.3981 | -48.89712 | 2026-09-20 03:45:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35d70b6c-b1f0-36db-8b70-a140ffa1af5e | -12.15613 | -47.03228 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3995193c-3d05-31a3-89b6-1398873c3e20 | -11.45406 | -45.36784 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5916c6e6-30a2-3fd8-aef9-7834355833d8 | -9.25283 | -45.93164 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9902de0f-019c-3061-a06b-d0628be80d33 | -13.02744 | -46.92629 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c9804abf-8ca9-3820-95f4-1de48bc8842c | -10.31644 | -50.22391 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d08a079b-7118-313d-b9ff-e3364d704a61 | -12.29416 | -47.11986 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd42d036-8b50-36f4-b86e-93c075f9a147 | -11.03062 | -48.30099 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54edf210-3843-39f1-bb19-b402d04872f2 | -13.0244 | -46.91285 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98473709-0873-357f-a87f-c8c4587305e2 | -10.30847 | -50.24808 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 000a278a-3a05-3033-8209-c81d204629d2 | -11.86554 | -47.64946 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dabe0615-eff9-3b79-afba-78294efeb5f2 | -6.99055 | -42.20067 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1c6fe519-b87a-3b1d-96ec-0e39bfe77847 | -12.69581 | -45.9437 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| facf800f-fee2-359b-9a41-9179f9039407 | -9.26187 | -46.21127 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8c15970-49ec-30d0-af10-9477ef096157 | -12.69062 | -45.9425 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7933d5c2-074b-385f-8586-caa306b5d166 | -12.01435 | -44.68687 | 2026-09-20 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4a0789e7-db57-3019-81cb-87ae455388eb | -10.32841 | -48.00403 | 2026-09-20 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e31c8f0-3e71-3bab-b654-e37278a560f8 | -11.87295 | -47.67422 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e6bce5f9-3b77-352b-a1a6-54993d732c25 | -11.45285 | -45.40301 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 292cd88d-e8c4-3a62-b621-1eace8a1f3e5 | -7.77153 | -49.19395 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 105d0271-2b00-305a-9b39-a9c79b1802a1 | -8.63621 | -47.62038 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1b20fcc-8b08-379c-b6b4-89ce6f2423eb | -6.20798 | -47.35892 | 2026-09-20 03:45:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a4f4ed5-bcf6-32f9-9dc9-ec665accc869 | -7.88032 | -44.87125 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a6d2ff7-98d6-3d01-86ed-8cd367b8385e | -6.29982 | -47.62779 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c48c9ce2-55b9-39e0-918a-038fd36d8f26 | -11.87665 | -49.00964 | 2026-09-20 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| adfa4f53-985c-3476-9eb4-3fe37a7a67d3 | -6.98101 | -42.17559 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f8c6431-b7e5-3c5d-ae1c-f7d264ed4426 | -7.77025 | -49.20057 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1378426e-2b00-3201-b7bb-10036669c1d3 | -13.28197 | -46.73397 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cf15880-392b-37d8-b67a-4aafad064bef | -10.99779 | -48.31445 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42491cbd-18b4-36b0-8a52-2204551b01f8 | -6.97652 | -42.17485 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40e4d668-33c1-36bc-b7fb-ded71da65cde | -6.81359 | -47.89193 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 695c1638-ce92-3957-81b1-eed2f96d5f44 | -9.259 | -45.92936 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2f40c9ec-4666-3a30-8971-a716d4e24cd5 | -7.53694 | -45.42978 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |


[Clique aqui para ver as próximas entradas](README16.md)
