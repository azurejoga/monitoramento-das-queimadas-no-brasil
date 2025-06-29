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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ee1b46c-5d81-362e-8c3e-1869b9c7d262 | -12.4811 | -58.459202 | 2025-06-29 00:41:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9ccbdb5-ec78-3e49-887a-602c376711cd | -9.0933 | -59.458599 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f67e9e5b-f5de-3bc0-b81c-56f1404e63f0 | -9.7244 | -56.178902 | 2025-06-29 00:41:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e93817a-91a0-3383-b97b-54cc6f9a1cd0 | -12.479 | -58.4491 | 2025-06-29 00:41:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87fe1650-0f54-3f33-95b9-7a5c40972248 | -17.3937 | -42.647099 | 2025-06-29 00:41:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b405c141-07d4-3ac7-8b36-c821e8cb2401 | -11.5548 | -52.783798 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3541d6-1ef8-3821-9320-0981b86f04c4 | -7.2994 | -55.3064 | 2025-06-29 00:41:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3247050e-fe35-323d-8ff9-352251f254e1 | -11.5466 | -52.793098 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a12e85f5-facf-3764-a725-140d44d99547 | -11.527 | -52.797699 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0b04cea-2e9b-3627-9e65-4601e5722610 | -10.5634 | -52.055302 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 688d7c13-e914-340f-8845-dd074a6b8312 | -10.8736 | -53.7407 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 026c01ae-79cf-3a3d-b717-69f5c5ef7690 | -11.5385 | -52.757301 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 295d6633-045f-35af-a223-6207003e0907 | -10.965 | -45.1147 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8dcd44-f424-3e18-a4b7-b2c5d5133c13 | -11.5156 | -52.792801 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8453a9dc-e259-32d2-a19f-9e37dcf21f88 | -21.023701 | -50.177299 | 2025-06-29 00:41:00 | METOP-B | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68e3b862-5d2a-3f78-89c3-8d2f24cb3f04 | -12.6156 | -57.871201 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abaa7947-1b2b-3682-bdfa-20b6535a288b | -11.2561 | -52.7397 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31616bee-1b99-3c35-8598-6f6733f92e80 | -17.387699 | -42.625198 | 2025-06-29 00:41:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbfa417-fd3b-39b4-94be-8f83ab7f9177 | -18.5016 | -49.7663 | 2025-06-29 00:41:00 | METOP-B | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5445853-e9f4-33be-8f59-cc5ba47f17b7 | -10.2979 | -57.123798 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 739769da-a0aa-303a-987c-ed3e85f63f35 | -11.0342 | -56.251598 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96e0236c-db19-3501-a1bb-44e35ebad463 | -11.0294 | -56.2766 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0d2625-a45e-387b-8e96-c6bec8b89580 | -12.0498 | -48.468201 | 2025-06-29 00:41:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58888154-fb41-3950-980a-2a6966274062 | -11.2675 | -52.744701 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26f95df7-4143-33dd-9e6b-86ca56d8fc1f | -2.7499 | -54.593498 | 2025-06-29 00:41:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac05da7-a988-31e9-afbe-76fa477cd5e1 | -11.5336 | -52.781101 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 386d5aaf-77d3-36a4-88b1-e4d2cbf909ac | -11.5123 | -52.7785 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5899660-986a-3b58-b92e-6b357588aba1 | -12.4929 | -58.4673 | 2025-06-29 00:41:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92dd71a3-b353-3ccf-ae2f-3fb88b915998 | -11.2773 | -52.742401 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8ce2bfa-3081-3c61-93c8-a084cfced08f | -11.5483 | -52.7551 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5ef141-3bad-3838-b9fe-61bdcbca1264 | -10.5518 | -52.049999 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04233b7f-0bac-3f5a-8beb-5b531c8076d4 | -9.7129 | -56.173698 | 2025-06-29 00:41:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80029a4e-b8e6-343d-b41c-a526bd16a6cf | -11.5613 | -52.7672 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6338cc42-3051-3c95-8519-0093561c2a46 | -11.5369 | -52.750198 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5457d3bf-1dfa-38c1-af93-c8e86c6599a4 | -22.406601 | -46.812 | 2025-06-29 00:41:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21a6540a-cf7d-3f4f-9576-707185c22c73 | -10.5616 | -52.047699 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2766fd20-0c7d-3e2e-9b35-f8bd4761256a | -11.5434 | -52.778801 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 325daad4-e057-3c7a-b8f8-551eea4ef078 | -12.0623 | -48.476898 | 2025-06-29 00:41:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 401e5e38-5d13-3ed1-bafd-b071a3864498 | -12.6039 | -57.863899 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 405ad00c-95cb-35c9-9b28-3539e0864a95 | -10.0358 | -54.324299 | 2025-06-29 00:41:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbc09a9-f03e-3b37-ad6b-8808e310be60 | -11.0097 | -56.2332 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb6af19-5188-36c7-a3b5-19c962dbb5bd | -11.5515 | -52.769501 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1be72b19-8d0a-3e8d-b837-5bcf9cb97aba | -10.5581 | -52.032501 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1255a82b-203b-3245-9990-444153685468 | -11.5384 | -52.802601 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6eff707-13eb-3121-9418-ee27a45664e7 | -12.0525 | -48.479301 | 2025-06-29 00:41:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05c18421-8375-3579-902b-19b189ee3bcb | -11.576 | -52.786301 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33463487-a4b5-3aac-b694-49295c4d58e2 | -12.1075 | -54.6632 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6d95883-e0f0-3e61-92bc-a61533604e90 | -10.8473 | -53.761299 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6a00b8-e803-32c2-8aa9-734ee1b46515 | -11.545 | -52.785999 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4af6001-d143-3929-b341-d01e700b4294 | -11.5286 | -52.804901 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 675747c4-34f7-3dc3-9fdf-61ab7a3ad2ff | -9.4699 | -57.328098 | 2025-06-29 00:41:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c463005b-bd8d-319f-b311-811256423cfd | -21.020201 | -50.162102 | 2025-06-29 00:41:00 | METOP-B | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9291077-96ac-39cc-942c-a45951a32aae | -10.9697 | -45.0928 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c02eee2-aa9f-389a-8f4e-f6b74a3dd459 | -11.5532 | -52.7766 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96506eb5-992e-3726-b494-093297b80745 | -6.6165 | -47.2817 | 2025-06-29 00:41:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94350ecf-bf98-3b07-9996-124352144e2b | -11.5303 | -52.812099 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edf7248b-6d2c-33f0-80d4-1d2004cbf446 | -10.8654 | -53.749901 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8b1f64e-8804-35d4-b403-1876cb97d873 | -11.5221 | -52.776299 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b61ec4d-89da-39b2-9ee2-4f6a103d549f | -12.623 | -54.199799 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce15dac-aea3-38d3-bade-d93224442c0b | -14.8445 | -52.284901 | 2025-06-29 00:41:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6752633-066c-325f-81ac-63547a0736c9 | -10.9796 | -45.131401 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2014c2ce-fd39-37ac-9833-5760653a6a82 | -11.2577 | -52.746899 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5917ef3d-b2b1-3ed2-83ad-99f2ba0a90de | -11.5238 | -52.783401 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80d8e933-7c95-3380-9c66-836c331c7cac | -12.6058 | -57.873299 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f74a214-3f3c-3856-8fe3-6e13c2e277bc | -11.5565 | -52.745701 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7ec3978-5a5b-3918-80a8-8da7ea2c5824 | -11.5646 | -52.781502 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2456bdc-5fc0-3627-af68-39ec9da2338b | -11.5271 | -52.752499 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 714b054f-ff41-368d-8dcd-3afe013f8b39 | -11.558 | -52.7981 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e58369c9-c977-3830-88bb-a7e11f31e8fd | -11.0179 | -56.223499 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f76efd05-b35b-3e20-814f-2c34c32d9ab4 | -11.5662 | -52.788601 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e20b54b3-6512-3476-a3e4-2e337a2e5039 | -11.0359 | -56.259201 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f958889d-0641-3736-ba56-64714f388723 | -11.5499 | -52.762299 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6a366c3-80fc-39c2-b985-b2b7ff21ff4f | -13.0181 | -53.425701 | 2025-06-29 00:41:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36d9b9f0-6fc1-3d74-a4fd-e4b6bb7b8f6c | -11.0212 | -56.238602 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2186841f-390f-3c23-ab1b-5d797c08357c | -10.1627 | -53.9244 | 2025-06-29 00:41:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb0538c-b38c-387e-baad-5b1dbd9fff8c | -9.0976 | -59.479401 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcd2f6b-299d-3ed8-a436-1ca2cdfab1dc | -10.2969 | -57.023102 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81286fda-d138-33b7-8cba-a916c11ffb1c | -11.5728 | -52.771999 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62e66d2f-4efd-3c42-8b28-95b6e7634274 | -9.6394 | -48.7906 | 2025-06-29 00:41:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6097a128-3c6e-38be-9d02-5e287b762c06 | -11.545 | -52.740799 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7a8839a-1d53-397f-932e-690f8e9833dd | -10.3459 | -57.492599 | 2025-06-29 00:41:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bedbec9-755a-3e7d-82cf-89d57e37bc69 | -22.3943 | -46.8046 | 2025-06-29 00:41:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64041d10-bf2f-3500-bf89-ca8a16084855 | -11.2659 | -52.737499 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b39bd36-bc66-3c5a-b932-0f22ee34f4b2 | -10.5714 | -52.045399 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc48319f-7346-3776-a8d0-962ed69dca8f | -10.3077 | -57.1217 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d63d2cbb-6a8e-3e6a-9d3a-bd60945e94f0 | -13.1405 | -56.803501 | 2025-06-29 00:41:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7ee99d-0d46-3430-a4cd-fd581e618758 | -9.475 | -57.830101 | 2025-06-29 00:41:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90f4407d-d52b-388f-9af5-f7e1eecdd928 | -11.5678 | -52.795799 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 384c8b72-6100-3662-8f42-825197856397 | -11.5287 | -52.759602 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0ce8fb3-3735-3120-af91-da8dc36c41f3 | -11.5303 | -52.7668 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cddf5405-9ef6-3e9a-a8ce-7a3900ae5ff5 | -12.1085 | -54.5742 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e32c1665-211b-3010-83c0-e253e29e8d29 | -12.106 | -54.656101 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea8eab3c-b064-3147-8784-4e5b66356cd8 | -11.0326 | -56.243999 | 2025-06-29 00:41:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb567424-c60d-335e-ba1c-40a1ff7a1343 | -10.9747 | -45.112202 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4281175-c0a9-3581-8c52-2ab1c525cd8d | -10.3557 | -57.490501 | 2025-06-29 00:41:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fab3d5cb-7145-3363-8302-9843f5e4da2b | -11.5401 | -52.7645 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c2b9c14-b7be-3670-b295-9742d7f29cac | -10.5483 | -52.034801 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2feb1383-0299-378b-b3e4-e1ff89d00295 | -6.6262 | -47.279301 | 2025-06-29 00:41:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a79b4b-26aa-30ce-81f4-8bb3b5cbe2c2 | -10.8375 | -53.7635 | 2025-06-29 00:41:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bafdfb07-b203-334e-80bf-876f362cf7bd | -22.396799 | -46.814701 | 2025-06-29 00:41:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
