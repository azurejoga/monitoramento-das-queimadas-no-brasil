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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bbf14bc-1b03-3044-89e9-b89b70f643df | -3.48801 | -54.78556 | 2026-01-17 04:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45601ae5-3976-3598-97b0-110c41c322d9 | -8.42802 | -44.01801 | 2026-01-17 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13d4c918-8a23-3774-a29b-1f9919e6eb75 | -5.56601 | -45.45478 | 2026-01-17 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7a8bab4-4d13-3f7b-afb3-867eb00b11f5 | -3.67063 | -48.92965 | 2026-01-17 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af744667-5807-3ab4-9092-d1f838d2433f | -8.43206 | -44.02411 | 2026-01-17 04:46:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 734bfadc-6d13-3f68-b919-324ff7e2516c | -2.93155 | -48.2325 | 2026-01-17 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da57160-a2e8-35cd-8deb-347899757637 | -8.25256 | -48.28941 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f9d1982-ec22-3dc7-909a-aa4d91129334 | -8.25684 | -48.28568 | 2026-01-17 04:46:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a11de347-31d7-393f-adef-bab2fbc6b826 | -11.8016 | -45.36342 | 2026-01-17 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1ba68790-f8e2-3ef9-92ec-10cd60b00ce2 | -9.6529 | -46.23354 | 2026-01-17 04:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91192d5d-ccb3-3857-9a71-38975c67e926 | -10.483 | -49.35849 | 2026-01-17 04:48:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e51d33c2-95c3-34df-b2d7-67c30f6f2453 | -12.6561 | -46.76495 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf8d8804-ad06-3a77-adec-ded446e1521e | -12.65186 | -46.76434 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a648b596-fd7e-3508-9369-1164980ba4d7 | -14.71838 | -53.96169 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 064c8df5-bc92-3067-bb49-333a84aa35a7 | -11.88159 | -45.70081 | 2026-01-17 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa504426-1fa5-3ad5-afec-cb181dca4705 | -11.23381 | -48.09382 | 2026-01-17 04:48:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10a79772-ec88-3d1a-88fa-a9e9b4ac073f | -14.72113 | -53.96587 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f87570f-9f11-339a-a00c-c7de1aee08d3 | -11.797 | -45.36278 | 2026-01-17 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| afe4e03e-6509-3755-8806-de753754f63d | -10.93525 | -49.42678 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4fed924-34c9-363c-85b0-d415bb65b56f | -11.01321 | -45.25276 | 2026-01-17 04:48:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 421a400d-6fdb-3951-b4ad-5d19ba623e56 | -13.6923 | -55.68316 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| dac646c4-a63d-3d33-a52d-cb24de784ee0 | -13.94887 | -48.51372 | 2026-01-17 04:48:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d254ce1-ac35-3eba-b973-527c7c46c424 | -10.34236 | -44.82771 | 2026-01-17 04:48:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5de3495-9248-3faa-9baa-5d0b812d0ac1 | -10.93464 | -49.43082 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97033c49-482e-3bfa-bb4d-ab3c5fab6419 | -14.76876 | -45.93288 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae2323fd-24af-3958-9a23-e0ab124fa810 | -14.72055 | -53.96947 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6d6528-3cdd-38c5-b3eb-531029293ce6 | -15.1277 | -51.4244 | 2026-01-17 04:48:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e141fa42-e362-3a70-9afa-cdfc002cc551 | -11.83786 | -49.19611 | 2026-01-17 04:48:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac019dd3-94cb-39f1-a850-5731dae15263 | -13.28094 | -53.95852 | 2026-01-17 04:48:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 553ad2d6-e70a-3252-9426-4399946a5744 | -12.65719 | -46.7569 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c870e6a0-b317-3e86-8774-843f1bb883d0 | -11.16099 | -43.57493 | 2026-01-17 04:48:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffd0a5c9-f9d1-3c74-a770-57eaec700027 | -9.76763 | -48.27115 | 2026-01-17 04:48:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 577d78d7-4470-3f70-9264-5a78264fcddf | -10.4824 | -49.36251 | 2026-01-17 04:48:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 324ed861-40ed-3f2e-a8e3-19daf2394899 | -10.56195 | -44.32086 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54ca1c0a-1a6d-368a-9317-770ea8dc0db1 | -14.71505 | -53.96113 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ca646f5-dc35-3976-9f27-9f6c4b6862d7 | -15.01896 | -48.66541 | 2026-01-17 04:48:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e549316-973a-3279-914a-ad2a886f4ed4 | -10.81436 | -49.2933 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 996858b7-cf05-3e05-bb84-575df6d45de2 | -15.89201 | -43.45474 | 2026-01-17 04:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2cb6106-422d-3061-bba6-2ad01d78f19d | -11.28587 | -48.73011 | 2026-01-17 04:48:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16b0976d-56cb-3572-894e-fa1e25350de1 | -10.93092 | -49.42948 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c267827-c563-3e9a-8296-1cd44b3be940 | -14.71564 | -53.95753 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a930a46d-91ee-38f3-a411-0e88f2ccfd39 | -13.69438 | -55.67091 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0197118e-e18d-36f6-95f8-45af2e272cb1 | -11.01258 | -45.2575 | 2026-01-17 04:48:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca3817e1-753f-3e71-9aaa-9392ce1710ba | -12.08228 | -43.76622 | 2026-01-17 04:48:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7feb8f09-1398-3edc-9ebd-a37c5262d0b4 | -12.91849 | -49.48656 | 2026-01-17 04:48:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fc1a3e9-1313-33fe-8624-4fd49999c931 | -12.22471 | -49.64053 | 2026-01-17 04:48:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b65cccc7-0e8d-30f4-9ef3-ddb194395aec | -15.05419 | -46.85374 | 2026-01-17 04:48:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4993d670-103f-3730-bb31-e359340d0b19 | -14.74759 | -45.9151 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2bb832a-1adc-3660-957c-4940d6839851 | -12.65979 | -46.76955 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85065d66-eeac-3b03-b144-46e1f8e9c1ae | -14.75096 | -45.91748 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b854dac3-fd7d-34d2-bbe4-01c4dc13e16d | -13.69161 | -55.68725 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833f3763-ba25-36ce-8845-173ff5f4c6c8 | -9.77134 | -48.27171 | 2026-01-17 04:48:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 278ac60e-20a2-3ca4-b502-2e69e0ba4e95 | -11.80684 | -52.39093 | 2026-01-17 04:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb2fd681-4319-35f6-968c-609a1c8c0b33 | -14.71172 | -53.96057 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6d1a4b3-77af-35ca-9e87-6bb8d7085d6d | -14.77625 | -45.94084 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b4e72bf-b11c-3fad-801e-01895ea852bc | -11.79636 | -45.36759 | 2026-01-17 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a3955b9-26ed-372b-9f69-b39416ca2def | -10.71402 | -44.15212 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c03b8831-2e35-3a50-8247-fad2cf66a62a | -11.83725 | -49.20037 | 2026-01-17 04:48:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6889eb0e-6c09-30e2-bf96-9eec7ae86147 | -10.16599 | -50.81472 | 2026-01-17 04:48:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33d8c595-ce3d-3b41-b9f7-eaecd4458de8 | -13.69015 | -55.67437 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552bce24-86f1-3e8f-bab0-7be370817589 | -10.93109 | -49.43029 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d8b30ac-1fa0-38bb-b8e0-adfbd1fddd10 | -9.65233 | -46.23747 | 2026-01-17 04:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a05a9aaf-152a-36b6-9641-3bfc3232a134 | -13.69584 | -55.68379 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a8eeec75-e1d3-37ec-8428-12403c92c2af | -11.84514 | -47.92223 | 2026-01-17 04:48:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fee5913-fee1-35e3-bd37-1149e8ad8e74 | -10.34674 | -48.9204 | 2026-01-17 04:48:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3e75053-9edd-3e4c-9e67-99fd15b9b161 | -11.83664 | -49.20461 | 2026-01-17 04:48:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b720a23-4e33-3053-ba20-25cebd88e773 | -11.83664 | -49.19711 | 2026-01-17 04:48:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f2a6414-0df9-36da-a14d-e237c7b6e02b | -13.70076 | -55.67623 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55fb0e45-1c2b-3080-b845-0b895ee636a9 | -12.08742 | -43.76704 | 2026-01-17 04:48:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c50b1ecf-6b80-3da4-8661-f317649a7afc | -12.65556 | -46.76892 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f69d2dc-2f81-3b93-8e3b-ccdc4d591df6 | -11.83601 | -49.20135 | 2026-01-17 04:48:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f1c0f02-2d61-3f18-89c6-09879424adbf | -14.76479 | -45.92737 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 859752c4-f716-31ce-8ca1-02154a4df668 | -12.6524 | -46.76033 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09a648e7-2a87-3635-a42b-74cd3f19f667 | -12.65664 | -46.76094 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c161437-7e42-3c2a-a2ef-e8749f00e17f | -15.01826 | -48.67045 | 2026-01-17 04:48:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d9f8338-c7ae-3b76-9c7b-483742303907 | -15.89244 | -43.45104 | 2026-01-17 04:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b76bdee-1b33-3379-be29-17e002150106 | -11.80352 | -52.39038 | 2026-01-17 04:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa020066-e010-3807-9991-74f8022bac48 | -14.71722 | -53.96891 | 2026-01-17 04:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41578782-1d44-33eb-9db4-f5fb3a6bbac0 | -10.93447 | -49.43001 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 713fdd1a-58f8-3204-84b3-e894ccd1ad40 | -13.69938 | -55.68442 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 06d862cf-0a72-3e8d-ba36-2e1bc79b1241 | -14.75221 | -45.9157 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 304bbc68-431b-38f8-ae53-3584a4fb57c6 | -13.69722 | -55.67561 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4efdd4a-3b54-32e9-a7da-48d4575859a6 | -12.84857 | -49.86645 | 2026-01-17 04:48:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd04b597-7b58-3c6f-b7c6-b226b35927d3 | -11.32169 | -44.4985 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d918e759-98a6-3870-97bc-79ec2281d809 | -11.83105 | -46.59443 | 2026-01-17 04:48:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2637fa3-1973-321a-8df5-6f0a8a4eeaea | -13.68591 | -55.67782 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d3db41d-77f5-32a9-8c4c-54b9dfb4f400 | -12.65295 | -46.75629 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fd593add-5ddf-3ca5-b142-ef7e021d7736 | -10.8108 | -49.29277 | 2026-01-17 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 355f4877-f794-3892-822b-7b9675d094b4 | -14.74823 | -45.91017 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28848150-5e85-3540-90e2-f9d00642258b | -13.70007 | -55.68032 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0dc8d976-0be2-33c7-8364-af174c3c9255 | -10.41275 | -44.88945 | 2026-01-17 04:48:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2184e30d-cc3e-33fc-9ef6-9845da0bddaa | -11.04768 | -45.41013 | 2026-01-17 04:48:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18777010-21e3-391b-8ee3-32894cb797a8 | -14.78026 | -45.94635 | 2026-01-17 04:48:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6af97c2-c958-3cc6-b8b1-d091b5a2213a | -10.81154 | -47.56824 | 2026-01-17 04:48:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b07ae6a3-29f2-363c-a934-a9826c0ca657 | -13.69299 | -55.67906 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d05ba458-159b-3ac5-a256-35de4dd04847 | -13.68876 | -55.68253 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daa5228d-332c-3571-a5d9-a9d6ff9bec4e | -13.69369 | -55.67498 | 2026-01-17 04:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be15f3d6-e1c1-399c-a052-091e821bd041 | -12.66033 | -46.76557 | 2026-01-17 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d1f7602-b358-3e10-9a5a-299d0591484b | -9.65653 | -46.23808 | 2026-01-17 04:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e88aa2f-cb2b-32f1-91b4-e4a4205d9c60 | -9.75893 | -48.27874 | 2026-01-17 04:48:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
