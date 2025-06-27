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
| aa314aac-2776-30da-bfb4-34b48925919d | -10.65345 | -44.48795 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c652afe-81f0-3129-a085-a9524c927126 | -15.72157 | -43.49306 | 2025-06-27 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcc9f24d-ff13-3f0d-b9a2-7f574740b904 | -10.2735 | -47.60349 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c15ced2-bda9-3f39-9d30-d0105e743d79 | -11.5729 | -52.11401 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5b6809f5-4e1e-3fe1-bc32-d3574a19b21c | -11.81225 | -47.52538 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b616b3f-9ae4-353f-a1ed-9a1160472b7a | -11.05689 | -55.37027 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 308b02c2-aa10-3f13-8a2c-ce2bb9c7e017 | -12.03274 | -48.75422 | 2025-06-27 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2c1d893-0281-3eab-a976-55aefc784c54 | -12.41997 | -46.66811 | 2025-06-27 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c9563fd-461e-35b5-a034-16b982676249 | -14.20736 | -45.51202 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a608221-ab88-3fef-8431-c411ba131437 | -12.75642 | -45.08767 | 2025-06-27 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ddc617b2-34aa-34b1-9789-45b1da29ffee | -11.57916 | -52.11849 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 153428be-7532-3210-aa20-61b41477fb38 | -13.76229 | -52.31453 | 2025-06-27 04:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03df605f-3a03-39a4-8127-a8cf7ef96047 | -11.11983 | -47.01106 | 2025-06-27 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7780469c-41d1-340c-85f4-00e835b0e8ba | -14.43902 | -48.86697 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85eadfc1-3cba-3df9-8153-e685de3ec0df | -12.02734 | -47.77655 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e9428301-eab1-3b80-b0a7-4b5c004e224a | -12.43301 | -43.72593 | 2025-06-27 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db0f0dc8-c19a-3a53-98e0-4ce568f28331 | -12.04817 | -48.07904 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 570ae0dc-03c0-3a5c-825b-397b06aa350f | -11.06163 | -55.37465 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 015be371-d188-3d50-b577-a24fcf3ad238 | -11.06634 | -55.37917 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1aa511c-ac89-313e-9fd8-f603513867c2 | -11.67885 | -46.72681 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 035dd62a-83ed-346d-aa07-3d348339ad30 | -12.16328 | -45.01306 | 2025-06-27 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82b3ab06-5b95-33b8-9e62-c08b30ea82b0 | -10.302 | -57.13517 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d1402cb-63af-3527-8754-79d7f166a538 | -9.35354 | -58.84901 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cffb6fb-fc79-35b0-a1b5-87a294a6ab28 | -13.58654 | -45.25845 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fdc7066-9353-3c61-b9a1-90ad08c08e52 | -9.78572 | -48.57559 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d26c84df-23d1-3084-ae3a-261d1343f4b3 | -9.49739 | -56.09504 | 2025-06-27 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c6d6e4f-f329-3d62-bf73-b651aee7511c | -11.44224 | -54.46711 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f7e86cf-5cbf-3935-9dbd-ea74b3d5d0d4 | -9.87543 | -48.44727 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b18de0b-5751-3fbe-bc12-799dd03b49d4 | -11.44674 | -54.47094 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0925ba3-b2a8-39f1-a9d8-d4db17b9c8ef | -10.08506 | -48.2999 | 2025-06-27 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9808c506-f840-3842-bb0c-26c5ba932245 | -11.99485 | -47.15551 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ef35118-35e1-38a0-9b8b-4e796b97ceae | -11.77552 | -45.21535 | 2025-06-27 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe00e442-6f73-3001-8695-b2ef0bcb2258 | -11.06098 | -55.37812 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d2ecae36-d31f-3c00-b31c-406825c220de | -9.11386 | -49.43123 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff96b98a-1e26-3786-8fb2-c69a0554e149 | -11.57638 | -52.10945 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7c93821b-9461-31db-b29c-bc013c74bae3 | -11.44062 | -54.47588 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8db8efa-2434-37ab-a628-63d057f3216a | -12.75258 | -44.41021 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e8a5d2e6-c83d-38d3-aee0-dc8b9c39e9d9 | -11.44278 | -54.4642 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43e86225-8102-3659-8b48-5677b8224300 | -12.76731 | -44.40483 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ebefad6-74a0-374c-9256-cd4e6b4cb142 | -11.44728 | -54.46802 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f35ee6a-971d-3888-bfee-1eb1cefe4893 | -13.92995 | -54.49875 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b0cb499-e9fa-311f-a67d-62c91c621f99 | -8.33488 | -55.0979 | 2025-06-27 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acad115e-e6b4-3b54-8bc5-891be90833ba | -10.30806 | -57.13645 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17dc07b5-6f71-39e8-9d8c-ebba2588de3f | -12.55203 | -46.9073 | 2025-06-27 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a66c971-91ab-3ac9-9039-19365d9674cc | -11.57792 | -52.11059 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f748b6d2-5182-3476-951d-622e83ab08bf | -11.0717 | -55.38023 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 645daede-65df-3b41-b041-ece8c340686c | -11.57719 | -52.11475 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| de6caf99-2153-368e-a855-fbed824d2244 | -17.04486 | -43.77359 | 2025-06-27 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 85c79ddb-b976-3007-8410-8653bda92597 | -11.44171 | -54.47001 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 208101c4-fd08-38a1-ae53-3a2ebce2828b | -10.29473 | -57.13618 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae4b9c72-8837-374f-8c49-e300470bf9c7 | -11.07412 | -55.07483 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42b1027c-a825-370b-b69b-0c00e89fd069 | -13.94541 | -54.49609 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b9868bc-801b-399c-bbd4-f6e962658696 | -9.82112 | -48.38043 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89e24181-b4ab-329d-95da-fce38ac7f004 | -11.60226 | -55.54122 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e75f628-007d-37c6-b814-dcba3f7b8106 | -11.77565 | -55.03474 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c8a4a1-6bbd-3b0b-8324-8036b3f4c791 | -13.15977 | -45.22824 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c44b57b8-334c-3244-b596-c5b9ef3d6766 | -13.70395 | -48.4006 | 2025-06-27 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf6df554-fe57-3e5b-9f8d-bb26aa236e16 | -9.24755 | -48.75005 | 2025-06-27 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da1a836a-8534-34ca-91a5-a23a4668dcc5 | -11.84217 | -43.79574 | 2025-06-27 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a977baaa-ddcc-3ad8-8017-a80c262bf295 | -10.30714 | -57.14108 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eab1fd0-c679-31eb-9798-0fe986799238 | -14.24014 | -45.49871 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cff6384-6c64-3ffd-872c-71501dadeddc | -11.57574 | -52.12311 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 706a7f27-b393-33f8-ae27-d0808abf9903 | -13.05412 | -48.82056 | 2025-06-27 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab358803-a284-3630-acad-ce804c1ec0fa | -10.53051 | -53.62241 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3408a6d2-e5fa-3e05-b82d-adfad8e48fa5 | -10.6264 | -46.68903 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b029472-188b-3986-bdc7-e0b388e3f7df | -11.36095 | -48.71043 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb1d6544-d52a-3d5c-a15f-78e333f2e7fc | -12.01095 | -47.16182 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a1d46e-b277-30d6-8510-5add756924c6 | -14.09652 | -41.87637 | 2025-06-27 04:21:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 130b27a4-273d-361b-bbb0-044d0f804c13 | -14.66735 | -53.12573 | 2025-06-27 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3ee8275-3cd2-3b95-8c4a-6fca0396d4a5 | -11.35871 | -44.89483 | 2025-06-27 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ac2fd81-aea7-30cc-b6b7-f8a8829d62b2 | -13.09316 | -47.14281 | 2025-06-27 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d75980-4f19-339e-9801-c047e2c9fb59 | -14.75774 | -48.17597 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa2b16c9-21d4-34b4-9a6e-39db97fb2364 | -13.06181 | -51.63987 | 2025-06-27 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2280baba-1af8-3270-aa38-07a1adc11fa2 | -11.921 | -54.80997 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 098e2103-ded7-3ae0-9072-8a7328b395f7 | -11.36515 | -48.70699 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a57df566-c83d-3386-9b3e-df4cbc5a8858 | -10.83153 | -53.7369 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4114c70-859e-352c-b0d5-64819c9dbf3e | -10.86792 | -53.77542 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94cfe82-adc9-3075-9c25-17425443cd1c | -8.62139 | -51.58464 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b5d7330-0081-304a-83db-1485d342ffe0 | -11.81994 | -47.54177 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e6e4a7a-5f69-347a-914a-67b698d34822 | -9.07676 | -49.41778 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1544235d-f662-3ed4-a62f-4f0957ea2c63 | -11.82175 | -47.53073 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ce4a7eb-6a7c-33b1-92f0-de937b74762d | -10.24407 | -47.45801 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f5b8190-c67b-32a4-b484-563ae6534501 | -14.44246 | -48.86758 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81a18f9f-e059-3a5b-bef3-f6e858f7f685 | -12.00486 | -47.15716 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51e4a4bd-ca34-3931-a0a7-a2d60d611844 | -11.67829 | -46.73032 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80779837-465b-3243-b4fc-2eb2ab061b73 | -13.29253 | -57.09389 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30e06c70-e6e1-33dc-9a32-3734192f8f5e | -11.57563 | -52.11359 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f0186f9b-311a-3361-ab7e-471ae5661530 | -13.16311 | -45.22878 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 706fd2e6-61ae-3e42-9e7c-9ea4cab3869b | -9.35268 | -58.84845 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be605cb4-020d-34aa-9204-4fcb8e506596 | -11.57487 | -52.11775 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 869b7b97-86be-3690-989c-6c5771a28ddd | -12.02636 | -57.08209 | 2025-06-27 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c79fb98-46da-3b2c-884c-bbf079e75595 | -9.78918 | -48.57099 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86c0ecc8-0197-3efa-b86f-359c2ff63355 | -10.29594 | -57.13396 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84a45819-582e-394a-a641-84243f01695c | -11.60538 | -55.54126 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8929b523-3727-3ac1-b412-c371318c849f | -9.11308 | -49.43582 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecd46b47-a945-3953-b476-9353c21e4482 | -12.00152 | -47.1566 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1120bcd9-aee1-3223-b0bb-d3f9af1d635c | -11.58148 | -52.11551 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 077bf6f0-2516-3390-bf3d-828314bed828 | -12.43009 | -43.72147 | 2025-06-27 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a204a3d-b9b2-325e-bc2c-960acf57e14e | -11.77804 | -55.02203 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d729fefc-a65a-3824-b20b-59101013b328 | -11.58735 | -44.66875 | 2025-06-27 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
