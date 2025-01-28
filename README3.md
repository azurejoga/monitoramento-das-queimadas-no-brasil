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
| 78c6700a-c32d-3505-9d04-ddb445e2e500 | -3.3839 | -53.23582 | 2025-01-28 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad704082-a0c9-353c-8dcb-492a9ced0c69 | -2.91015 | -54.28915 | 2025-01-28 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73c73824-0efc-39bb-9737-bd987b9c642c | -2.90681 | -54.28861 | 2025-01-28 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a418ce7-beb6-3fb6-8af2-71e353012cad | -3.58711 | -53.71015 | 2025-01-28 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3916d88e-7e0a-3f25-be95-01a8d8cbae2b | -6.34071 | -47.09892 | 2025-01-28 04:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd76f38c-d877-3d53-ab0f-74c27c37769a | -5.23554 | -56.06206 | 2025-01-28 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acf6f25e-37b3-3ad9-9f02-9d0490ac4838 | -6.22239 | -55.65807 | 2025-01-28 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67664fff-1bba-3c8e-9ccf-b9c5400c3b0d | -6.26374 | -48.03587 | 2025-01-28 04:57:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 538788b6-b211-39ea-999e-f471de0db3cc | -3.44364 | -52.73351 | 2025-01-28 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe9cd935-e126-3ecd-a2c6-8b86336c4173 | -5.00752 | -56.17718 | 2025-01-28 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 78e74d1f-4faf-376c-9673-4806cb8f3559 | -6.27261 | -48.03691 | 2025-01-28 04:57:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ed1bb1d-c1f8-37de-9b2c-c54c8f27f5d9 | -3.45944 | -52.86213 | 2025-01-28 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9a4e3d-a77a-3e2a-a9cd-896e097d2369 | -5.27416 | -45.76932 | 2025-01-28 04:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d68df95f-f18e-38ed-8984-4a25e852bd11 | -6.2688 | -48.03214 | 2025-01-28 04:57:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d013f1d-e9c0-33d9-945f-9a3d18be44dc | -6.33952 | -47.0971 | 2025-01-28 04:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96b14ed7-0e0f-343a-9175-335b5bcbef15 | -2.87617 | -54.87264 | 2025-01-28 04:57:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e6be3e-50d3-3236-9108-1ea7b4a89075 | -2.16528 | -52.44992 | 2025-01-28 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c35c5e70-cc5f-3bf3-b6dd-a6f8e526fdb1 | -3.71962 | -53.75211 | 2025-01-28 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e16cd68a-3968-3fc4-b563-18a003b7990a | -6.27322 | -48.03275 | 2025-01-28 04:57:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82e73c64-e719-30a6-8077-d82a9d7cc90b | -5.32503 | -55.94301 | 2025-01-28 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 953ac510-c0de-3c3d-a465-b3a57611e772 | -6.50114 | -47.48917 | 2025-01-28 04:57:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6765b44-5810-38c9-86ca-043f78c0e7fb | -2.81771 | -49.01777 | 2025-01-28 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49183ca4-29bc-309e-86c7-50279618be2e | -2.82242 | -49.01338 | 2025-01-28 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d0295f1-1f5f-3b08-bd1b-5c81f377bfb8 | -6.34139 | -47.09402 | 2025-01-28 04:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ed6bef5-ce6d-37df-aa48-e631533e7d97 | -5.39075 | -45.28549 | 2025-01-28 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22e42453-92ca-360e-a9ae-21ce92c4a27b | -8.3169 | -55.11884 | 2025-01-28 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fe7c3e3-c404-3d6a-8750-328a18a4bd23 | -3.56256 | -53.30974 | 2025-01-28 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04d35ac9-42f6-3bae-9d93-91cbccde9bf7 | -3.17451 | -48.69875 | 2025-01-28 04:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 724b2681-10e8-3627-be89-26db4aceea49 | -6.54343 | -52.95305 | 2025-01-28 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9e76133b-c806-3bf5-974a-d90b46e9b97f | -6.26818 | -48.03636 | 2025-01-28 04:57:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c5825c4-c9aa-35e8-ac05-53639a502a13 | -2.98455 | -54.58777 | 2025-01-28 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5fcf97ac-9423-3ab1-8df5-ace9b0577635 | -6.50034 | -47.49088 | 2025-01-28 04:57:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9136d931-7976-3b4b-89e5-03b760754cfb | -3.38722 | -53.23634 | 2025-01-28 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adf11691-2c54-3b26-a2d3-34f635727f7b | -5.02216 | -45.96751 | 2025-01-28 04:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c152120b-299b-3d4e-9202-81268d0c5671 | -6.49651 | -47.48867 | 2025-01-28 04:57:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20cc2a04-eb06-34dd-a2e6-339ecdc61b55 | -6.54173 | -52.94166 | 2025-01-28 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b8e6313-d91d-3a40-9210-e7ba3fe6d628 | -7.79686 | -55.0289 | 2025-01-28 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0436673-b130-3edb-8d78-6ba657da1161 | -5.27373 | -45.77232 | 2025-01-28 04:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b56079d-5cf1-33d2-b5d9-cbe53bca8763 | -5.02245 | -45.96539 | 2025-01-28 04:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcbfcbf8-d3ca-3fda-8045-dc227c3771fb | -6.54682 | -52.95358 | 2025-01-28 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3aec002-e3e3-3683-8d72-c3ced55bfbfb | -2.9812 | -54.58723 | 2025-01-28 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 351edabd-169e-39ec-8e0f-060a30d7624d | -6.51972 | -52.43399 | 2025-01-28 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc247bd9-e751-3f69-aa4d-d24e628ca240 | -12.69989 | -54.89834 | 2025-01-28 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c71efbf-767b-3a4c-81be-6df1296e09de | -12.69878 | -54.90552 | 2025-01-28 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5858e119-06d8-30cb-aaee-d5d236d7a972 | -12.10103 | -51.22267 | 2025-01-28 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02a2a397-3fcc-3100-9ecb-076cc8c04ebf | -12.61433 | -52.46047 | 2025-01-28 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc6a944-cdd7-3ca5-9ad9-34ecda9d3acb | -12.69484 | -54.8865 | 2025-01-28 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d89a9a5-ea50-3a27-8c40-4968a9a9d76b | -15.07623 | -48.94233 | 2025-01-28 04:59:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 448ebb79-594c-35c9-989b-5af64a0b667c | -10.69143 | -54.35623 | 2025-01-28 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78fdf138-6474-331c-9efe-2d390ce955f8 | -9.26031 | -60.31442 | 2025-01-28 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79c49d3c-a027-3d39-b6d2-e63518689443 | -11.05712 | -45.38057 | 2025-01-28 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76eb0ce8-17a7-361c-9c5d-9ca828c4b1fc | -12.09688 | -51.22366 | 2025-01-28 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f143b703-7550-3633-b293-1b83d0c92cd7 | -10.68752 | -54.35928 | 2025-01-28 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e30b601-696a-3886-999f-b2531e759e58 | -11.05429 | -45.3821 | 2025-01-28 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3143361-6e97-34f7-8885-816fe103c306 | -12.09713 | -51.22211 | 2025-01-28 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 790f2c4a-52f4-30f5-b9a5-0ad6e0ae98d1 | -12.48542 | -43.78642 | 2025-01-28 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 736f5c92-dc5b-311e-b0a9-bd8b0b511e6f | -13.96973 | -49.62488 | 2025-01-28 04:59:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0767cf59-dc9a-3699-9e49-12a8520b0149 | -12.10078 | -51.22423 | 2025-01-28 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6c4c48-5212-3224-b3c9-8dedfe58b7d6 | -9.25844 | -60.31731 | 2025-01-28 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c31772d-22f6-3e74-9d33-1a9b0524e218 | -11.19103 | -55.53346 | 2025-01-28 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19792eff-0912-3bd6-a081-e9e51bcfbfe9 | -9.25909 | -60.31363 | 2025-01-28 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa046369-b9bf-3bc8-b17c-3f731b80a5b5 | -11.14555 | -55.56218 | 2025-01-28 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c946a90e-e306-3b13-bbe9-f6bf83fd4231 | -12.48482 | -43.79165 | 2025-01-28 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f9d836-a1f8-3eaa-b9dc-3738b223a9ca | -14.55731 | -53.97425 | 2025-01-28 04:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eff24331-569d-3056-b5b6-cd719954552c | -13.96528 | -49.62431 | 2025-01-28 04:59:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 167f811a-8506-3d20-9d85-ca746c97c549 | -9.25969 | -60.3181 | 2025-01-28 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e186b47-b65e-3219-90af-1a0bc95c553c | -9.79494 | -63.26096 | 2025-01-28 04:59:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f69ecf34-7439-3e8f-b389-d948632d6d0b | -11.58234 | -54.41029 | 2025-01-28 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3863a0d-b432-38d1-8183-3c138c602471 | -12.34872 | -47.99522 | 2025-01-28 04:59:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b7f622f-9c07-36c6-a7fc-1253d185b0cc | -14.43116 | -54.0512 | 2025-01-28 04:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2755213c-3832-3866-985e-1d75451e2105 | -11.05144 | -45.37993 | 2025-01-28 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b457981e-a220-3095-aae4-b529fb130f80 | -12.70493 | -54.91019 | 2025-01-28 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ebaeb4d-6c94-315c-9549-b3e870db6b06 | -12.35355 | -47.99595 | 2025-01-28 04:59:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d650d75-0b17-366a-a6e9-278d059dd69c | -20.90686 | -56.53769 | 2025-01-28 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 847fc255-eee5-353e-807b-d5dd944c4115 | -29.61172 | -56.4556 | 2025-01-28 05:03:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 727ace20-a34c-39fb-8cb3-ad4b6e6e61da | -29.61535 | -56.45624 | 2025-01-28 05:03:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 6da0161d-0e49-327d-8cdd-b0c581e382fe | -30.87955 | -53.33138 | 2025-01-28 05:05:00 | NPP-375D | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 5e4492d7-5aba-3503-9df5-9f05e29de6d2 | 4.18443 | -60.60831 | 2025-01-28 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0938199b-3cf1-3b41-9214-49fdd021f57c | 4.3243 | -60.85868 | 2025-01-28 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272cbd19-9b57-3f35-ab45-a44e4e7aca53 | 4.49498 | -59.96586 | 2025-01-28 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f282732-341f-3a98-a8e9-172223d55720 | 4.3237 | -60.85478 | 2025-01-28 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 557edc1f-b1ec-3031-bd13-d813ce9a0db1 | 4.87197 | -60.50952 | 2025-01-28 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c53b0b-31e6-3cd7-b8c7-c5afa3e3c0c6 | 3.78652 | -60.00942 | 2025-01-28 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98d1b8e-50e1-31bb-b226-37f0623fe92f | -2.82283 | -49.01662 | 2025-01-28 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a03bea51-05bd-3ef3-9637-5561db002439 | -3.18861 | -54.51122 | 2025-01-28 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fce51eb3-db44-3e2c-8f02-7cbdc7762f1d | -3.18805 | -54.51491 | 2025-01-28 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bea61562-de0d-3565-ae88-b3bf8c83c1b4 | 1.3865 | -60.79768 | 2025-01-28 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bd23eca-2796-3e5e-a892-38f8dd991a02 | -3.11512 | -59.92871 | 2025-01-28 05:20:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8592d92-c7d2-3183-b4f3-1964b8f97061 | -2.92764 | -54.20722 | 2025-01-28 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a25d85f4-4778-351c-ba31-984fef7c0d2b | -2.70434 | -59.43119 | 2025-01-28 05:20:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ff574e-f293-32af-a4a0-7c5a4e636d45 | -3.43006 | -60.40931 | 2025-01-28 05:20:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 869f5c2a-0850-3441-8717-881bb6be4473 | -2.81686 | -49.01582 | 2025-01-28 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c638ceb8-7ced-3ea2-a5d3-b92d2fdc5298 | 0.59802 | -60.46684 | 2025-01-28 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fde2aa4-087c-3b7d-9b33-c62b505321b2 | -12.61355 | -52.46107 | 2025-01-28 05:22:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c43e205-b9c0-36e4-86e3-42e6f2932406 | -8.62495 | -63.48495 | 2025-01-28 05:22:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dcea3dc-85f9-38ba-a0d1-5fb42dc553f0 | -6.26211 | -48.03904 | 2025-01-28 05:22:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b4b36b8-7d7e-3f2a-adb5-d1b25cb12802 | -9.82286 | -63.56215 | 2025-01-28 05:22:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a81203a-d3b6-3004-967b-292cc0efaf3f | -5.23769 | -56.06129 | 2025-01-28 05:22:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a527734f-ef65-3461-816c-0195477ede71 | -9.79499 | -63.25879 | 2025-01-28 05:22:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2176d716-816b-3356-9a2b-bb6026405838 | -9.79841 | -63.25936 | 2025-01-28 05:22:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
