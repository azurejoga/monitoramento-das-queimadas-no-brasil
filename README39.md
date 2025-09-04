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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d201f21c-341a-3122-8378-4d3bf3e5d030 | -13.53012 | -47.01977 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6866580-57ef-3034-9b1a-9c081080d3f3 | -11.88482 | -51.53765 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94a31419-d92d-3855-aaa3-1714f2350e02 | -8.89536 | -45.81603 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62019113-1268-3e7d-a7f1-c7f8e5eea95b | -11.54677 | -47.31744 | 2025-09-04 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c1677d2-2eaa-3159-b01e-f9a43e3db16a | -9.49907 | -46.53194 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d81ae3a9-bc61-3735-aed4-498573d2c679 | -14.99848 | -50.07033 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a6e8b1a-a253-34e7-9bad-39e0aeac474a | -12.90445 | -48.05214 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 914a2e37-7b25-3eea-84b2-5f25ab4ebd84 | -13.4003 | -47.06871 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22a50201-486f-30e1-93e5-21e8f2abd6ba | -12.90501 | -48.04861 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59b1e492-2449-30c7-8dc4-d275a2dd2ecc | -9.97901 | -51.62383 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53d60c20-6f95-3aa1-8fb9-7dfdb18996da | -11.09648 | -52.02271 | 2025-09-04 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6aef1c90-5a94-3415-91f4-b085fae1214f | -12.50515 | -48.06262 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edea3a48-919d-3108-afdf-96d5f3f45a7e | -10.98721 | -49.73363 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8c51411-bbf4-377b-9238-765393d9fe53 | -12.48537 | -48.07761 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5619bda8-0327-3692-9994-0f1f0c2eaa7d | -14.77764 | -48.16761 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f895c08-0b8c-37e9-aa16-d222d781be2b | -15.00925 | -50.06825 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96227daf-d684-341f-8ab5-616d1d26e959 | -15.04269 | -50.06267 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38b61b64-71ea-3b72-a9cf-ea3a0693683b | -11.59389 | -47.75571 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f29c6f5-3d65-3d57-b16c-34edd6bc0a5b | -8.4407 | -47.33996 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aef757aa-047a-3851-9cad-e466fa19cf97 | -12.4831 | -53.82972 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ba6378b-b044-3222-b0f2-b3032fbb6528 | -11.04385 | -45.14709 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2346e989-1f03-3fe6-b639-5ec1b9c4ea85 | -14.28648 | -45.22838 | 2025-09-04 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff2f8eb5-81a7-392e-86e9-6269902bc52f | -9.43816 | -48.09042 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccfeac89-307f-35d2-9214-297fd76ca3e2 | -15.02946 | -48.09986 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa625e7c-a268-35a2-a2aa-3ec851e79736 | -9.97822 | -51.62844 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3434142b-14c0-3471-9230-a67af70e5ee6 | -14.39581 | -51.6668 | 2025-09-04 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c39672a-f327-3fbf-b007-57f02a0332e6 | -15.02678 | -50.03275 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8b5a351-7b9b-349b-bd95-711f9c288c0a | -13.73562 | -46.9411 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70d01a15-29fd-3cab-a793-b3471a420f0c | -15.02891 | -48.10344 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fc748be-b25d-3a6e-af72-3e2d66e306f7 | -13.74847 | -46.94674 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55033de5-7f3e-3d75-b228-48eab7d4132f | -15.04019 | -50.07778 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55047bc1-d9af-3124-a417-722d60e388f2 | -14.58959 | -48.02082 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94b38b28-b233-3b82-95d4-1328b60a2cfb | -8.08189 | -45.35725 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8208fb72-c5aa-3299-83ac-95c317a4890b | -12.2289 | -45.05946 | 2025-09-04 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d926891b-99cf-3dd7-a034-0d81f371cb2a | -12.91164 | -56.99567 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7d6608e-9e00-3295-98e1-4c810b89cff3 | -8.00492 | -50.09973 | 2025-09-04 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f5f6120-fa06-3f23-a3a1-baa01926d5ab | -14.21091 | -48.09266 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb03578-2440-3d42-844b-ffedef7153d6 | -7.73111 | -48.73117 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5ba80f2-708a-3cb7-9a50-d7e57a6c7c7d | -12.90563 | -56.94405 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b20815a-f1f4-3f07-8a89-827f594a53e3 | -7.79816 | -52.13602 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd953e5-e6fe-3b16-88ed-0f05f4c5e539 | -12.81535 | -47.66614 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d796930-27a6-36d9-9310-d54d2c743586 | -12.60727 | -56.9959 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed80e547-6ec4-3b23-8fdd-296ac0b9ff77 | -13.57141 | -48.13628 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bd139c3-5800-373e-95fa-5f6f7c1c43b0 | -8.43849 | -47.33247 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 101d2292-457d-3373-9430-4d15a1ef0968 | -13.86515 | -47.97796 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47b330ee-82a9-30eb-91b9-c85cf0997cb4 | -12.89126 | -48.02833 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c66d57b-221f-3dff-8f63-9bfbaef5a476 | -8.5314 | -51.31177 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 00f9efb3-5c62-3b14-89b9-0448c0abefb5 | -12.29647 | -50.00384 | 2025-09-04 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bdffc72-afca-32bd-8294-8a6359c22429 | -11.6005 | -47.77832 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 33fd68d9-89ef-3a26-870c-549e53503550 | -15.02206 | -50.08229 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2e325a1-2100-3712-8d4b-2e7586b52b45 | -8.3717 | -48.28831 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a665360-bedf-34c8-9033-25a3ce931e08 | -7.3888 | -56.68975 | 2025-09-04 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb6ba62c-21d6-3386-a5c3-96eed1d1b787 | -15.03778 | -50.05027 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e711caa-37d1-3919-8335-fe47cabb1521 | -12.49867 | -53.84093 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 890029c2-1321-3975-ac46-9148fad1c34c | -15.00616 | -50.04448 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c24cb4b-0d20-3256-9fe8-e8f92572b09d | -15.03497 | -48.10805 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7d96c49-411c-3efe-889a-e1822f6fafa3 | -14.5962 | -48.02191 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f7aff03-3acb-3f0a-8000-f92ad49467b2 | -11.57996 | -52.16281 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bce596f8-d5e9-35ec-aa63-6145c1c6c155 | -10.43591 | -50.36786 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| e9808078-d375-3dd3-af8b-e8d1382865ff | -7.70047 | -50.28455 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1127a75-355e-3c4e-8015-e2a5c64d6e9b | -8.64822 | -45.76348 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e34bce9-c0aa-370f-b799-6766e2c52326 | -12.96322 | -48.06942 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fc69d10-f902-3023-8d95-3566ccf57d25 | -9.56683 | -48.24206 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ee97c6f-ca76-351c-8ddc-398a7af0fd3a | -11.85486 | -51.44445 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22d07d76-b1f8-32fb-bf6c-ee7485223228 | -11.85332 | -51.45341 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59144aa6-f8a6-37e1-82a8-71f1e7fc2e75 | -12.94341 | -48.06618 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f72b9c2f-c180-3079-ab15-4bd80e3c2fd3 | -12.23583 | -50.15712 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2607b08-7fe4-3c36-b47c-6b19c2d0f390 | -13.65597 | -46.94715 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65318ac4-4af1-3872-ac42-b1c4cf1a335d | -15.06277 | -50.04629 | 2025-09-04 04:27:00 | NOAA-21 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d3a46c1-0876-34d2-b150-9c57602e045e | -8.32368 | -47.39214 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80db5f63-1738-3d42-8e77-263dc99fac31 | -8.73458 | -47.00584 | 2025-09-04 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e770e05e-6124-3417-b470-3cecb180e639 | -12.18252 | -53.88277 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07f20382-59ea-3c46-94bd-2174be701443 | -10.47816 | -53.63135 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b212e799-59cb-3aba-8e02-8c4ccac4f578 | -11.05426 | -45.14865 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 76759c2d-d80a-3021-92ab-1cbd16e39e5c | -12.99076 | -48.06667 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5f84c08-3b1a-361d-aa03-dac64daf4b67 | -14.90782 | -49.61784 | 2025-09-04 04:27:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c418b9a4-718d-36c1-828b-109c7c778d8a | -10.47908 | -53.63445 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feb9b15d-dc7f-3297-8e27-e37f85b68808 | -10.9962 | -45.91391 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 757d8f8d-cebc-3cf3-a5d8-529f71190ae9 | -14.75639 | -48.08417 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1dbf39f-fe7a-3582-aa07-96b43f6194c1 | -12.8621 | -48.01998 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ba558b3-fad8-3d28-ad9e-8c35fa397675 | -7.72769 | -48.73063 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58f93625-db98-38e1-aa37-effdfd1a5356 | -14.80789 | -48.2345 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d92035a6-1b73-3af4-aa35-5eae3c5e4098 | -11.61759 | -52.18283 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b850dd60-a48a-3ffd-988b-6293929ff038 | -11.58069 | -52.11184 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ea7de652-bd97-30db-926e-791ceec6d0e1 | -15.04394 | -50.0551 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b093a7d3-c77a-3827-99dc-9b4be2fa800c | -14.29012 | -53.09829 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce6bde7-2e43-3ff1-91e1-688e051a4bad | -12.43927 | -48.71246 | 2025-09-04 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90cf030-29f3-3ec3-9523-53ce41ddab91 | -15.00738 | -50.03697 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 438edf70-10b9-38f4-b0d1-3438bf6bbeed | -12.18109 | -53.89096 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edfbfa3a-adcb-31f4-a3bf-8bc66ce0aa29 | -12.94011 | -48.06564 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46e4bd96-eddd-3fba-913c-f1e7464a4adb | -10.44517 | -50.26817 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 486b04c8-363d-393d-81af-b9319a0a64ad | -15.00248 | -50.06711 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 340cee82-03d1-3779-8c47-8395da8d9c89 | -10.26905 | -54.26798 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78801cb4-fd33-3325-894d-3a59ca12ebbc | -10.75652 | -45.26705 | 2025-09-04 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b324ac47-08ff-3556-9452-b5714dc2117e | -12.92591 | -48.06647 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 757e12ef-b8ed-3258-8787-79b41be8ccb1 | -9.74915 | -49.46222 | 2025-09-04 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dffae2c1-6c01-3eb2-90a4-a87109074a56 | -7.71006 | -50.29499 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de046457-a047-3093-bfab-b16f231c3796 | -15.01292 | -50.04565 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24fb4371-ef10-3424-9a5c-f2ee168402d5 | -9.70437 | -48.95632 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 995cc93e-e3f2-3880-90f7-744506a5173f | -11.53921 | -54.48713 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
