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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22c954cd-78d6-3911-85f4-d867cae8320b | -2.7343 | -57.611401 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f366aa4b-0786-3600-912f-ea002e036387 | -13.8361 | -49.684101 | 2026-10-08 00:26:00 | METOP-B | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f96d896-5aa7-393d-bd09-caffb798a46e | -3.0144 | -54.051701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36100c2c-a896-3850-bad4-b22cee70d3c7 | -6.667 | -55.075901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e22e18-bca0-3682-8a68-c76b6557601e | -5.8786 | -53.496799 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd8dd498-52e4-3142-81c4-2112594bb757 | -2.8723 | -54.8815 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73aed067-c1bd-3eed-bcfa-672430539ac9 | -3.2867 | -54.070702 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf360372-7e26-307c-b968-ae08d02918b6 | -20.73 | -48.971199 | 2026-10-08 00:26:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5817b37-17b2-36cd-ad5b-5fe0277c036d | -6.2202 | -52.7775 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ec27ab-967f-3e8a-b7d6-08e2008a356a | -2.3443 | -55.692902 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40919a49-2899-3874-9f52-f8b6463ae5a4 | -3.8503 | -58.883099 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba6c5829-2586-3c67-a8d1-60632133f0d0 | 1.8599 | -55.746399 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35d1d013-da78-3266-a2a4-960a1709130d | -3.5344 | -59.497002 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd3f862-d96f-3109-a0d2-27ebfc654cdb | -3.251 | -53.867699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23c12292-1b65-3bcb-bb33-63a980e1f64f | -3.5266 | -59.322601 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee3e219-e0dd-3f05-8bfb-fece6fea28f4 | -3.082 | -54.304401 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72607600-9fa7-32d9-8ed6-42a29b61f06b | -5.1628 | -45.3283 | 2026-10-08 00:26:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b47ee84d-ffea-35a7-b84c-24270fc42636 | -3.5554 | -54.665199 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f3a957-ce18-32bb-aa10-4546bb4d72f8 | -1.7545 | -56.185001 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f58f6d-df93-3846-85a6-a66bacb6c8be | -1.209 | -55.686401 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75b819da-fccc-3453-bae9-758110ed7959 | -3.5342 | -59.403198 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62aa93ef-d518-37cc-9735-0a5d91170b5d | -6.5172 | -55.373901 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10306a15-c282-3c17-a27a-5bfbaa44c928 | 1.7063 | -55.605099 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc89207-7bfa-3736-88fe-1a1ab47d4b05 | -2.4577 | -56.058601 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d55b5620-3707-33b1-9133-369f5c665f1f | -3.9011 | -59.438499 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da42efcf-1e2e-3ac1-8386-44bc34a8d145 | -7.5972 | -46.755798 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2584f0bb-6050-3cd3-a7bb-d5e1cf4d73bb | -3.2977 | -54.665298 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f64e2643-6331-3498-88ae-dc5cffc5c464 | -1.1114 | -54.1619 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbb73c62-fc1e-354b-a5a5-2b366bdc96f4 | -3.2667 | -54.6651 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f6c75a-7ce5-32fa-8879-64f018775e84 | -3.3023 | -54.685799 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea80085a-f1ad-3b16-bdd5-af4efc6849cd | -3.4744 | -54.625999 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f98ecbb-5859-360d-b8a8-bd2406fd34c1 | -6.3186 | -55.314499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df4b77e-4837-328c-845f-28911d190f8c | -2.9583 | -54.122398 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15326e23-2b41-3c37-b100-13a51828b693 | -3.0735 | -54.1763 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2221e089-8ad4-3416-9a3c-714581269170 | -3.0902 | -54.2953 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4b13db3-e541-3485-8310-1e7abc989120 | -5.3729 | -56.0602 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1474eaf-53f8-34b2-8b73-ed893521bfab | -2.5628 | -56.1595 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a856020d-0ab1-30b9-9e77-c2e3a9ca40d9 | -7.2115 | -55.116798 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4488796c-29c4-3589-9862-d94b202c17d1 | -5.2359 | -55.999802 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fadb4a99-04d1-38c0-8ddb-effa9b1e7140 | -14.9249 | -48.085098 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6a96df-a060-3670-8260-d0dae2d2a2b2 | -6.1532 | -52.6646 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3c7ee3-a0e3-387b-9b94-76ff0f6c0108 | -4.2972 | -54.800598 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27b5237-b5bc-32b3-a192-e433a27f2dff | -13.4999 | -44.368801 | 2026-10-08 00:26:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c87caaba-f330-36e4-adcd-82ddfd95aa99 | -2.9469 | -54.117699 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48200cad-d68e-3971-8bd9-b63871d60e88 | -1.8087 | -57.111801 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce3415b-11a2-3bec-b792-d457037a8932 | -3.0789 | -54.2906 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9667062-6f52-355f-b7a7-b7a9dce0a93e | -3.5115 | -54.6535 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4237c629-7e0e-3e29-8eb2-b8567544a44e | -2.8471 | -54.132702 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6c999b6-19f5-3969-b52f-85894f448d5f | -2.9994 | -54.0769 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556aa0cc-bb46-3da2-8d23-fbd128b59fee | -3.7322 | -58.860298 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da2adc9e-0cb1-3335-acb4-b6641e1ca4e8 | -3.2923 | -54.004299 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3a96b8-7aee-3869-93a5-682f4e06e16f | -6.2294 | -55.653301 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b90b36cd-2a8d-386e-be46-aeba6ea446bf | -3.1684 | -50.5811 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8207eb98-90ee-3a10-a95d-4b1e02893678 | -6.2495 | -52.8606 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4651196-714d-330c-94fb-430fc1be3185 | -3.2754 | -54.066002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f81197-68f4-32e5-866c-f57f28d7a787 | -3.0063 | -54.744499 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 935112a8-4de0-3871-964d-702b63f26c29 | -7.8521 | -49.275299 | 2026-10-08 00:26:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8beabc38-de56-3b09-afb5-b37deafb16b9 | -6.3928 | -52.991699 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f4bf0e7-8802-398e-a6ce-16e885930abe | -3.0383 | -53.929901 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6ed4b4-29c2-3f7c-989a-dddf8ea0ecd6 | -3.2954 | -54.018101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fdaf761-6e10-3bf3-9687-76588493dbb3 | -2.4978 | -58.071499 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 286075d3-9d48-3cc3-82ea-850fa715b399 | -1.8561 | -57.047699 | 2026-10-08 00:26:00 | METOP-B | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96596bf1-a925-3a24-8139-de02fdee0399 | -10.4457 | -47.269199 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e69d65a-f287-3732-b162-8ba9ac7ab812 | -3.2303 | -54.321701 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 895941f3-d98d-3475-9f4c-c984527765a6 | -3.0539 | -57.476101 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdf31b8-c82f-38de-9ccb-b070a7839a5e | -3.006 | -54.242001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbd84eff-6574-3a86-841d-da4cde55700f | -2.2275 | -58.105301 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea828718-fdc8-3a7b-82d1-10cc05291655 | -2.3957 | -57.891899 | 2026-10-08 00:26:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd20c19f-d6f6-3419-a5cd-c7ef470ab8f8 | -3.4312 | -59.540401 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 325712c1-f79c-3e03-86b8-9941a76edcd6 | -3.3038 | -54.6926 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea9fa40b-3c6c-3fc6-8947-eed5dba07b05 | -6.0193 | -52.755402 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 529ccfa5-92f1-37ac-be74-80ae29de07f0 | -2.5499 | -57.386002 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06bb0c73-0fec-3de9-a6bc-78dbd0773005 | -2.851 | -59.1007 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a911ad8-8ea8-3093-96eb-5ba73ae9fda3 | -9.5824 | -48.911999 | 2026-10-08 00:26:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eedbd9b-1c11-36d3-9b6c-8f23e3115436 | -3.1144 | -54.1744 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cabb91f-bcf8-3af6-b7b7-e5dc86a0ac15 | -7.5781 | -55.006001 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02108c8-e601-34d6-b8f9-b5cc103ceb1e | -5.8113 | -51.713902 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed22cb4-7b1f-3888-b66c-9945ad47d099 | -2.3916 | -56.1315 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a4fa00-a197-347d-acf0-5aaad5ed63f7 | -5.9891 | -55.6838 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a426495f-5ccc-31ba-90b3-a66492204e00 | -2.509 | -56.149399 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184e6c3f-897d-3137-972e-efe3ab1b7a53 | -8.2192 | -46.351101 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab19daed-b041-336c-8258-e36e87196f61 | -8.7221 | -45.181 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a80e36ac-4cc9-325e-92a6-0e8417af3096 | -6.2218 | -52.648998 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d70ac1bf-4720-371a-80fd-19dd20508f69 | -3.1811 | -53.8321 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26ccb677-fefd-3294-8cc6-3fcac2f5b905 | -3.0712 | -59.2598 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7025c561-a793-306f-b2d2-7b51b60b5daa | -2.9422 | -54.097 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e47bf46-9dc2-3d8a-bbd8-a4efbc895a84 | -5.9528 | -55.3367 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0968919-40f9-36bb-b541-495da595144b | -6.1132 | -55.686401 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e17b5227-15c0-3e90-8dca-d6431b622537 | -3.5958 | -54.570301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 497a751d-822c-3ecf-94a9-6e66a83d42f6 | -3.1713 | -54.607601 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baece4be-da70-316b-b517-c5e07b35d708 | -3.0468 | -51.215302 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1839fb-dea7-3064-b203-dcff4cb97be7 | -2.9413 | -54.183998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8609da80-3814-359f-adc0-dbdc4e370168 | -3.5572 | -59.460602 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c881483e-9aef-3ba6-8078-fc0c150bb00e | -3.2282 | -53.8582 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 486bf395-b519-3b76-80ab-17a715c2dbca | -5.7452 | -53.454102 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4686d3f8-327a-38f3-b955-552293e38c5f | -13.8093 | -52.7864 | 2026-10-08 00:26:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 378e94f3-1982-3d7e-98e6-1aa43e91f689 | -2.8342 | -54.121101 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b710ebd6-72e0-3da0-9ae1-2a5ee838d389 | -6.7242 | -55.055801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f47b0287-ab37-38aa-ab56-105b34830cc5 | -3.2883 | -54.077599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3834753-6389-34e0-ae92-2f8277f6f5c4 | -3.1659 | -54.083302 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
