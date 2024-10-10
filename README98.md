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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dce12ee-f7ca-3834-a8b1-42fbf1dd90c4 | -8.35041 | -44.08937 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0bf67f8-f191-35f9-9aca-fa4e4e144269 | -8.34972 | -44.09442 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33178053-fbd8-3582-b366-dd9914acbbe7 | -8.34902 | -44.09946 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 130470d1-ff7f-3171-9952-369f385ebb65 | -8.34501 | -44.09372 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32ef5b3c-3a10-39d9-acf2-1635a4486be0 | -8.33962 | -44.09807 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9929253d-1d48-39ce-ac23-5c569cea9121 | -8.33492 | -44.09736 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26b82761-b281-33ef-af2d-5635f7e0f900 | -8.32953 | -44.10166 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d8b83c4-d9b5-3462-a522-0856b9c7b150 | -8.24347 | -44.8606 | 2024-10-10 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e533f4e9-d39c-34c6-8cbb-edcb1cd79674 | -8.13038 | -44.46284 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 719dbf87-c34e-3aa2-836a-a34ef2145fa6 | -8.1297 | -44.46762 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97d774bc-920c-3960-b67b-6ce91ca1b56e | -8.0572 | -44.78349 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea486ef1-3035-3b6b-ad85-ed5ee264eeab | -8.05662 | -44.78757 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9d310d4-65fa-339e-aa72-5cc8b9080dce | -8.00296 | -44.37236 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7638ec61-b735-38ee-ac01-788bf93eb5bb | -8.0023 | -44.37708 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ceaecf7-04b6-3eba-8f06-5459dae388a9 | -8.00163 | -44.38179 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 085b6d7a-8565-374b-8472-5b9b2ac5ed43 | -9.55919 | -44.43169 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3682e994-7f05-3cec-a61c-e472431271b9 | -9.55701 | -44.43075 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c879eeb-af30-3891-a7af-619d5a8f9e75 | -9.55632 | -44.43568 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30ac6399-98e5-3031-960c-a6fa539c6acb | -9.53292 | -44.43242 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11312e9e-966d-39a3-bade-be6d6b969a8e | -9.52757 | -44.43663 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5b2dd08-c0ed-3d06-baf3-cc3c6ea088e8 | -9.5229 | -44.43593 | 2024-10-10 04:44:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c7f52d0-eb20-3610-8c74-c61a786f4cf8 | -10.76333 | -44.99857 | 2024-10-10 04:44:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ec286b1-7f65-35f3-ba6b-77aef2db681b | -10.59715 | -44.77135 | 2024-10-10 04:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a60b252d-0cc5-3241-b76a-d7d797dd969d | -10.51159 | -44.85641 | 2024-10-10 04:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b366640-f1dd-3e58-9dfd-c6874247b13d | -10.123 | -45.20881 | 2024-10-10 04:44:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed2fa333-4c17-30bc-b17e-ef7a41c87ca5 | -10.12236 | -45.21348 | 2024-10-10 04:44:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54f78771-c6ac-39a5-a98c-56c7a6ab0ddc | -10.11849 | -45.20845 | 2024-10-10 04:44:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8dde013-ecac-333d-af40-d3ed8cba7141 | -10.6018 | -44.77199 | 2024-10-10 04:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94379ec9-8ad1-3cf6-b148-e24f4d55f61c | -10.60116 | -44.77684 | 2024-10-10 04:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e8df3b48-9f01-39d7-ad6d-5956a882c62c | -10.59651 | -44.77625 | 2024-10-10 04:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a61697b-59b9-351e-87fc-e2ff4f97ba5c | -11.13616 | -45.38013 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96bc8c55-9f93-3d2b-a84d-91fdc940a1ea | -11.14064 | -45.38075 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76d59a5b-d86d-3787-8404-9b1cb5d01f5d | -11.32626 | -45.82416 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 058a217c-8ec8-3987-8944-c94823c11525 | -11.13864 | -45.37812 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c553df88-1c50-3f51-8387-6ea98b41f935 | -5.08453 | -45.17028 | 2024-10-10 04:44:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c037f6e-f6fe-328c-9346-ed308f02364f | -4.90213 | -45.93739 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fdb5e0c-b53d-39eb-973d-9411a7ee6daf | -6.34127 | -46.30755 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa8e2b4e-0fd4-34a0-9405-5a58d8ae8ca2 | -6.30217 | -46.32735 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18278127-5b37-312c-ba53-e1d526ee68e1 | -5.98701 | -46.34636 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c25917cb-bd84-3585-ae61-1a3c22d86db0 | -6.22576 | -45.31256 | 2024-10-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0dc7d4f-6ec3-3b0a-b45d-6444effb5d3b | -5.91209 | -45.41838 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 852b3839-1b97-3136-aca8-dd395457265b | -5.91154 | -45.42212 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b0007e8-5c5a-3ed6-a6bf-ffda6a7880c0 | -5.911 | -45.42582 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffada0c7-0767-31fc-9d21-1b6a5b867aa0 | -5.90795 | -45.41774 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcb501cc-5e53-363f-a903-7ebadab4b033 | -5.9074 | -45.42145 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e2d753a-4d27-3ad5-8eba-6edb792c606c | -5.90686 | -45.42516 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| deac9519-bc31-368c-b17b-69d4b09b542a | -5.90381 | -45.4171 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e6d1333-9d1b-3279-a3ec-ff06a1bd8bca | -5.90327 | -45.42078 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de0ffc47-d2b7-359a-b64a-f75d891c4921 | -5.77661 | -46.11571 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71fb7e53-58e0-39a0-a59c-5acf3d301e25 | -5.6658 | -45.30617 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18fd77a5-2afd-3218-95b5-551094cb8e17 | -5.53604 | -46.19933 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 135356f9-40ee-393b-a667-1bd310147f88 | -5.53531 | -46.20434 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ee2ac79-7fbf-3326-ac45-aa4175be8d07 | -5.53082 | -46.15266 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce4d670-4c3e-3ef6-809e-d5be20438f40 | -6.335 | -46.07582 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db85d4f0-c30e-3817-a662-6154b1faa7f1 | -6.31461 | -46.40569 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c049222-97b1-35e0-9c65-1a59dda840b7 | -6.30609 | -46.32798 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b879a1cb-157f-33b6-9615-67812b6bed18 | -6.28205 | -46.35514 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7637985c-80de-37d3-9019-9f4753cf24cd | -6.22159 | -45.31181 | 2024-10-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 182ef00e-9835-38cb-ae37-2d333e1e1cf9 | -5.84913 | -46.43872 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7976bdd-6e15-3a9b-a3c9-331fed4a7d54 | -5.84626 | -46.45809 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4a7dcc1-e21b-3025-a7ee-44fd79e5a32e | -5.84309 | -46.45274 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80e4ae2a-545a-32f7-8535-8021d649a388 | -5.75928 | -46.5018 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 876dce8b-82e9-3c0f-bcac-f1157863dc9f | -5.7066 | -46.44685 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7961041e-09ba-3c26-8bd7-9effa2167e75 | -5.70463 | -46.4442 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07af12b3-958d-3d34-96d7-15e7b8fe8ae9 | -5.70274 | -46.44626 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3452d71f-ca21-3742-9a62-75cc8b98c0de | -5.70075 | -46.44367 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de491922-56f4-3497-93e4-356929faf2bd | -5.70004 | -46.44856 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90e1b462-47c5-30ab-9e2d-c970023399d4 | -5.69886 | -46.44573 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c2dbbd5-d289-30ff-8bea-f927bb1c97c2 | -5.68624 | -46.31934 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39aee8a2-6728-3bcc-bb90-0e41b31bdc58 | -5.58312 | -46.31252 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f02ec3a-900c-346b-b4b2-ff0a994d8c21 | -5.57923 | -46.31189 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4b84dc6-7c2a-3ad0-928f-0a02ea1e3965 | -5.55193 | -46.30814 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5d337f-4260-3eee-9638-f688c7539240 | -5.39592 | -45.98374 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76fad3f7-295e-3242-9a1d-f1d1140a3b73 | -5.39516 | -45.98883 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a36d1054-4d62-3f15-850a-13d5c2eb2866 | -5.39439 | -45.99395 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07a3b344-1bb7-3a13-b7f9-bdd0d5bf209e | -5.39119 | -45.98828 | 2024-10-10 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a99de9f-4ecb-3f9a-81be-f587b4fdf307 | -5.39064 | -45.40463 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba2a8fe8-43d1-3f19-b1d2-4e1a63c4802a | -5.38598 | -45.40763 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db27ee5e-2bbf-33bd-879b-6d191708a37f | -5.37032 | -45.19769 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b4a9b2-8f8d-3dfa-8a58-63f394dff0ea | -5.35377 | -45.70601 | 2024-10-10 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d737a998-34ec-3049-8435-b88b4dfb4ff5 | -5.31598 | -45.48432 | 2024-10-10 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c92d94b5-625c-334b-8b44-86f8c10d4052 | -5.31242 | -45.48003 | 2024-10-10 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45b17872-693a-3bca-b958-dd94ad03c48a | -5.31188 | -45.48376 | 2024-10-10 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9294936-318f-3d2a-a084-91f503fe5f2a | -5.26436 | -46.21915 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ae0dabe-82be-3555-9fc7-c461c1f50b8b | -5.26363 | -46.22401 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55f139a0-1e3e-36e7-913e-dac26cf361ff | -5.26047 | -46.21851 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae759dfc-9c9f-3e4c-ac90-feaaa0e217e5 | -5.25581 | -45.80193 | 2024-10-10 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18852ab1-43b6-34a1-8a45-3b8dad1201df | -5.20097 | -44.93727 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f537d429-4aec-3ad2-949e-4605f37ee4e5 | -5.19731 | -44.93265 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 988e42dd-d8af-3332-ba6c-d49740bf85d8 | -5.19674 | -44.93657 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9581103a-aedf-3ba8-bb23-515fb98e81ce | -5.14609 | -45.10142 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb700ae2-0481-3f88-a06b-4e7922190608 | -5.14294 | -45.10004 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf0f7f8f-09bc-3846-9f0a-1afe4eb11412 | -5.14192 | -45.10069 | 2024-10-10 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1a0ab5c-c1cb-3379-b3c0-2cc081ae3e88 | -5.09963 | -46.11644 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a18e265-9c33-36e6-8117-599703a4e059 | -5.0996 | -46.11487 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47b5b6b9-5068-3559-a874-d169969eef08 | -5.09886 | -46.11971 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eccd1b34-1b9a-314b-b238-cffbef3a09b1 | -5.09571 | -46.11589 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7f78064-fd4f-3383-80d7-fe5749d00c96 | -5.09494 | -46.11916 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 228b4d57-7547-31ed-8729-6d9e9fa85f3c | -5.05017 | -45.797 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06b9c25a-3ae1-3fcd-823b-94b1c27a31b3 | -5.04618 | -45.79642 | 2024-10-10 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README99.md)
