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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dfb474d-3a95-3cb9-9b72-6590959b2955 | -11.83154 | -46.45675 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 8b7300c5-9be8-3a30-89d2-6f278eb30305 | -9.43704 | -60.54569 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c23d087-9950-3032-85be-609e81c66880 | -11.36462 | -43.56767 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e29fa73c-6154-3bdd-9ab4-b488e7dea115 | -7.18555 | -44.04797 | 2025-08-30 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7d5a6dd-0492-300f-8d66-ba24d0a42e60 | -10.98712 | -46.84479 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c658ca4a-951d-388a-a681-14447edadb1d | -10.37257 | -57.83677 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a447a25-4556-3638-98a1-7916f9ef0679 | -6.7091 | -49.4498 | 2025-08-30 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7193d70b-195f-3c56-938e-8a7b9ea9313e | -9.43584 | -60.55207 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 748e32cf-16f4-3a8d-8c06-866ded976b63 | -7.21783 | -45.43516 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c788b050-f397-31f9-ad18-ed7292a54755 | -11.15139 | -47.14521 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ab09d16f-f7f9-3c10-bef4-fb0ee99c1661 | -7.08147 | -44.28482 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b8b012-9307-35a1-b309-45448cbaa496 | -10.68374 | -47.06476 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8a0a907-7f9c-3c52-a34e-e1585e1ddb91 | -5.99571 | -57.85305 | 2025-08-30 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c8656fe-f785-378f-aa91-764479fa1bc9 | -10.03202 | -46.03403 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d095cc4b-28a2-32fb-83bc-39b0997be400 | -7.63771 | -42.65958 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93fd17a9-f43a-395a-8178-d30127f9abd9 | -10.54094 | -56.38665 | 2025-08-30 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2201ea8a-f5a0-3052-aaab-b0ea5e637f86 | -11.15063 | -47.15053 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b54979b9-8e3d-35ee-b0b7-dad98c636cfd | -10.4915 | -51.62575 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 377e981d-642f-3c72-bd5e-aecb01d92a85 | -11.57878 | -46.36425 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eab73d5e-57ff-3e4c-9157-27862a4ace0c | -11.68267 | -51.68652 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9247ad8f-c42f-39bf-99c8-a1d4c9a10e6f | -11.845 | -46.39682 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db61fe57-2dcb-306f-ba9d-1a6d8da15cad | -11.06553 | -52.03891 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94dfcc2d-1149-3b94-952e-805b3cec2dc8 | -7.09644 | -44.31348 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c6882dd-e458-3b50-b551-cf31e074b750 | -8.70374 | -50.35985 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2768d150-fd9d-3173-b65d-4b53badbaace | -7.04378 | -45.82812 | 2025-08-30 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a289cd5-da23-397f-86c9-8d29cc815173 | -11.21998 | -45.02653 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 721a8687-5f60-3ed3-80a5-7b075c295ddd | -10.37684 | -57.83764 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c134b5ef-d596-3e03-94ad-ac10eb518743 | -11.84442 | -46.40093 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98c0a2fd-e82d-315b-a82a-894e44a02348 | -9.43607 | -62.36461 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 002ee431-2ff9-31cb-a5cf-2266b229e2fd | -11.32901 | -43.62407 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ff20fe0-b4c4-3496-ab0d-55cba08fad39 | -8.12341 | -61.21593 | 2025-08-30 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 795e111e-833e-3bb5-ae6b-d9e36abf4b82 | -11.14191 | -47.15454 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78fcd829-ee28-3fd5-99d1-b679b5df4936 | -9.2754 | -60.45883 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06d60304-58da-3ff0-9258-02d7d52a661a | -10.08359 | -48.8627 | 2025-08-30 04:49:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51e3bbb5-bf86-33b1-9758-bdceb21a1fe7 | -7.0919 | -44.31273 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a13a8cd0-7348-3b00-91b1-ae21a5fcf00d | -12.40303 | -46.48333 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58135b4b-0e16-3474-95fc-b36de2ffadef | -9.43755 | -62.32547 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 483202a5-2425-3659-86f4-64e83fc20014 | -10.37404 | -57.82858 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d4fdb1-2dcb-3052-a439-652ef6b27af1 | -9.63665 | -48.30021 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 923967a4-7ad9-3a81-85bd-65e15b5cd778 | -9.44015 | -62.34349 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6636e18f-433f-35e7-8395-8728fa3a2cce | -11.06386 | -52.04946 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0570becd-2443-3207-8981-c94c698b561d | -11.84877 | -46.39249 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 672458a8-5817-3551-a9c4-597e3e263ebf | -9.1246 | -45.20965 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de04c71b-684f-3ee2-afd3-e7aa0f2b1c95 | -10.64797 | -48.65044 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4500074b-feb0-3cee-936e-6bd279237050 | -9.15284 | -59.55606 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9adb6ec3-a915-3415-9edf-555b63c1be2b | -9.4636 | -62.34802 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2a0a2a0-4d82-338e-903f-e325ef5811bc | -8.17932 | -61.36971 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 415ddb0e-7615-3b21-a12b-fa6c81e4a3e8 | -12.36914 | -46.39001 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8137ced8-582b-34fa-a362-0226fb509115 | -9.44632 | -60.55386 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 66b73afb-23a9-3ec5-abaf-939aafff5244 | -11.73202 | -51.75581 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed25ccd5-3216-3b9a-8aff-d3bc2e64602c | -11.82678 | -46.46017 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e2a5d685-d258-3bdc-909b-dc4d70bf4f28 | -8.17792 | -61.37737 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70cd6e95-1271-3083-a571-16eeabdaf24c | -11.2197 | -55.06016 | 2025-08-30 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b69bd21-a3bd-38b7-875c-05e16033fbaa | -9.44695 | -47.63736 | 2025-08-30 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b32f62f-c475-39b1-8f28-a8a0331bdbcc | -11.83525 | -46.4612 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| d5f3e338-f033-34e0-8c68-cd6b159c1059 | -8.23753 | -47.20076 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ed110cf-f694-34f8-9c25-3bc49b848e1e | -11.3114 | -43.64007 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e508fa7-0e7e-3e67-9b3f-9127c5b5acee | -7.24688 | -45.44316 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db70839-1ff9-312e-b7d2-b2f680d29c5e | -9.44276 | -62.36155 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9776cb7-d1ef-36cd-82dd-ddec788bf972 | -8.18286 | -61.38223 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1501a2e3-7c35-38d8-855e-b4b706444287 | -10.27687 | -54.23798 | 2025-08-30 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c22d124f-1c9d-333e-b87b-291d1f0887e9 | -9.21862 | -46.75351 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b8fc3c3a-5b85-3e9c-8c53-70bef9c0b8d7 | -7.0962 | -44.31144 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2978ea99-8e65-3062-ba7e-2e3c7e0f8ab0 | -6.91413 | -44.38155 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfcadb89-7b7a-3527-ba20-0294e72098e4 | -9.43932 | -62.3478 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 89dfa1bd-2177-308e-9b8f-214e1b363d59 | -9.46201 | -62.35632 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 607cdb56-720c-3372-a7f3-ff3d86fb1e24 | -7.6007 | -42.72751 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dbf881a6-2e4e-3528-8855-d14cfd3aca39 | -11.30052 | -43.64431 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a365af9a-e570-3a7d-8c19-bbaa642639db | -11.30907 | -43.65796 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3eba013-ecef-337f-848f-6852189bacf2 | -7.72711 | -50.27088 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db7f3a1b-2147-3d4e-89af-f9cd08d300bc | -7.34461 | -47.53263 | 2025-08-30 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| daf329cc-4c1e-35f8-b8bb-bdf2cbed9695 | -11.9243 | -46.69336 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6ca38a0-d4a5-3c4f-a807-62916cb32fb6 | -9.17347 | -59.58279 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c21e47f9-ef79-32f5-bf1d-26fded2a577b | -8.84281 | -52.02263 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7183f7c-ad46-35ef-8370-4cd3dfe17504 | -10.34768 | -59.18833 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd1eeff0-e3b0-3973-a738-bcda13b9aa94 | -10.67974 | -47.06423 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b700022f-8497-3bca-8b13-db1354106ecc | -11.84403 | -46.42786 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b05b9a23-6f99-344c-8ff2-1fd471dbed9a | -11.33249 | -43.59753 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62bf9d32-983a-3964-9876-8a52c02d1dec | -8.34304 | -47.42357 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23812db6-aa69-369e-bbc8-ee52bcf39fe2 | -11.23047 | -45.01845 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ac50e50-cca9-3135-9830-51650c80b375 | -10.3712 | -57.81978 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c7d403-74e1-3f3b-80d1-77d8e9d41d45 | -10.73184 | -47.01303 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94830627-8849-301a-a5d8-1ba3438f65f4 | -11.3216 | -43.56166 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b18e96c-1b7c-32b9-bee8-cf0805697424 | -7.11916 | -44.60729 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 006dfe63-7f7b-3227-a30e-66dbb850ba55 | -6.86769 | -44.44918 | 2025-08-30 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f254046d-f75b-3cfd-afa1-5e809ad12b86 | -10.49039 | -51.63277 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52470620-d930-3cc0-ba53-390518fb4386 | -9.50143 | -45.39036 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 463da073-4d13-301b-8761-41ddd96b2bc0 | -9.44863 | -62.36264 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7064b1e2-e159-3887-98fc-8c083f102fc2 | -7.24504 | -45.45058 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 702023e4-1fc2-3cc7-9364-151cef72361f | -11.29582 | -43.64066 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d04e8ad1-63ca-3ead-a0ce-11258d9c5270 | -11.322 | -43.5586 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f8dd73a-264b-3fb4-a455-e0b22f8dc62f | -11.3047 | -43.5719 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdc043e2-ba4d-36b8-b350-3a575aa1abb7 | -7.60539 | -42.73135 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0c31a98-86d4-341b-adc5-e712e46db8e9 | -11.31062 | -43.60627 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dddb8c22-6c6d-3ceb-b009-1a7077f4569e | -9.43545 | -60.55507 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33933bbc-97cd-3cb8-9295-7a312a128e0d | -11.84396 | -46.39614 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20558645-da6b-32af-aac1-605c1532c893 | -9.43487 | -60.55827 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3db2f2af-5da8-30f1-89c8-0679b91b0216 | -10.84604 | -53.77211 | 2025-08-30 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe5e4f8b-395e-3ea9-800d-6cee15211b60 | -9.17692 | -65.5554 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 372e17ff-7982-3220-ad72-503ce508e5ae | -12.38759 | -46.43679 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
