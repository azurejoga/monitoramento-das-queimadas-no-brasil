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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01899159-e982-322d-9d52-915d72eee14b | -10.36266 | -47.89133 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db1bf126-0ea1-32e3-8847-65abc408c428 | -6.59946 | -43.59351 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3426ec-7da0-3a55-8ecb-e6fefa86e349 | -11.30066 | -47.41377 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 397b7e56-8ff8-3d5a-8af3-743eb2e56539 | -9.42447 | -44.71078 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 54bed693-2c35-3e42-a589-e674cf8c15cc | -9.43445 | -44.72146 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f17acd8-79e8-38ea-bbd8-e6391ea9c264 | -5.65212 | -51.4678 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bec7f00d-17e5-39c5-8547-7dd48d8d4280 | -9.42757 | -44.71594 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2649531d-fc87-327d-ae18-89b9b15f0328 | -5.64371 | -51.70498 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ac17767-e04a-37dc-9814-58ddd8c3a807 | -10.02333 | -46.262 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de89c23-8977-393e-899b-57c1691b125b | -12.08613 | -44.80003 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c98c3523-abf4-38e8-93fc-c01d74ebccc0 | -10.28256 | -46.07277 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 06ee9a89-1a5b-3b01-8458-27443fa4229e | -7.91658 | -44.10685 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40e67780-00b0-303d-9a72-f02b491b7dd8 | -6.2522 | -45.32901 | 2025-09-21 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e06325d2-d72d-3c2c-8303-01c54859a61e | -10.02212 | -46.26991 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42de801d-4fbf-3af7-88f0-c66ff8a4013f | -10.25495 | -48.06396 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6294c33b-3de7-3877-9b9f-30beddbf2a3f | -10.02505 | -46.27426 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 363b5cb2-d9b7-3eec-b1e4-79cde5f19f9b | -9.75825 | -41.88492 | 2025-09-21 04:36:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12ae9b02-5b48-3801-af93-489e6af879b6 | -11.31152 | -47.50241 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 39da85fa-bc80-3d95-9c88-780f4c270947 | -7.91276 | -44.10628 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73363733-61b6-33fd-9c3b-7b27ad691999 | -7.42127 | -44.54171 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d19cf942-ae85-3778-b057-a72ff6d74b8b | -4.48971 | -54.84392 | 2025-09-21 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc5013e3-fc17-33c3-95f4-b3b75a114e44 | -11.25894 | -49.8393 | 2025-09-21 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 338eecb7-ee3a-3850-bafb-5471eded1a40 | -7.91797 | -44.0974 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b95391d-e688-3af3-ba6c-30f8694d2906 | -10.23992 | -48.07257 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c682e76b-c98c-30be-9f5a-16dbe1fcaa16 | -7.92492 | -44.10328 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa6b4504-4402-3f72-9fcb-41fea4caf3c7 | -10.25774 | -48.06805 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 885e7241-a5f7-330d-991d-70de653e4164 | -10.27962 | -46.06824 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 872e8fa0-f7a4-3607-a7f1-e3181d394f72 | -12.07526 | -44.84067 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db5f4e0c-b8bc-39ed-94ee-ec37ec8139b2 | -9.16446 | -44.62303 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 91027946-6631-378a-bd5c-c285af988a22 | -5.79607 | -50.20414 | 2025-09-21 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 885ab411-bf7b-364f-af5b-5e25a76ed44b | -7.93117 | -44.11389 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3ffbdc7-1686-304e-8c1a-008202fb0648 | -9.42138 | -44.70556 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5b7beae-734a-356f-ad14-b3ce28762951 | -5.64837 | -51.46718 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4678e31c-df96-3adf-8354-3fe2bf360366 | -10.2816 | -46.07196 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d6f8f0e-4c74-38ed-8fa7-f7f26933102a | -11.77867 | -43.76513 | 2025-09-21 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad47b332-b3b4-3946-ba41-11f8af8bd566 | -7.92944 | -44.09911 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed063f49-c4ba-3bc7-8583-c24ab544bfef | -6.94555 | -44.76216 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3f27782-3ec0-3c04-a68b-d9ef634890f9 | -7.18476 | -42.24763 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3185a3a-ca68-3a72-92bd-58fc40770ceb | -11.02376 | -44.65186 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0479436e-0019-3429-9d8a-8dbe6cb34ba0 | -6.39091 | -50.9118 | 2025-09-21 04:36:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 594c5bd2-c765-33ad-85c2-9d4112ea7f42 | -11.27971 | -41.84987 | 2025-09-21 04:36:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8fb20413-cee3-3464-985c-04aec79985f0 | -6.33131 | -44.04951 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6f0c158-3c2e-309c-8e89-168fd6acf326 | -11.30249 | -47.51597 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec46f86e-c24e-341e-accd-5dac1b3e2d03 | -9.6408 | -49.65293 | 2025-09-21 04:36:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fa9060b-c545-3d11-9f1e-8ec7b55e9d77 | -12.07102 | -44.81536 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2aab2e04-efed-30fd-9c44-856ace98842a | -6.60378 | -48.01651 | 2025-09-21 04:36:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 839a6320-4639-3a24-95cf-c7f6634c96c3 | -11.28136 | -47.4032 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d1eb033-6438-3e26-ac52-a86dee77c100 | -10.2631 | -46.05761 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae66ea94-b548-3f80-a0c1-99727f048a4a | -12.08538 | -44.79813 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb59e8ef-d0f9-372b-9e26-9155f7d74cf7 | -8.25733 | -45.44255 | 2025-09-21 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63920c01-9fcb-349b-9dd1-d3137d3c7923 | -6.84849 | -44.17128 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed23b86b-d427-314e-8ee8-88f60f7f887c | -7.17959 | -42.24139 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de4bdc53-f9ef-36b5-aa31-0a7fc58ec50d | -11.76269 | -44.88902 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb7e5787-bb70-3138-a5f9-05213643b2fe | -6.41439 | -43.85391 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad1068eb-0918-35db-80c2-b98e809733fc | -7.60526 | -44.49827 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e9a79c8-1d9b-3573-a011-c665832ddf23 | -7.91971 | -44.11215 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3295c0ea-47ed-32c8-a7ab-5499556ba3b0 | -5.69775 | -51.75682 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2504659-4955-39bd-8fae-fb2ff3672713 | -8.48884 | -48.2656 | 2025-09-21 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e24b45f2-529d-3456-9698-0da9e5440c45 | -7.47574 | -46.66303 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fd8b640-6ea3-3867-b742-eee779d5a0c8 | -11.29854 | -47.51909 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bd17b24-fd1d-38fa-811f-d68289ed4dc9 | -6.41817 | -43.85466 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f471ed2-988a-325e-b9d9-134f98235830 | -9.061 | -47.01267 | 2025-09-21 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cd83d06-d445-327b-8701-4d9b326801a0 | -7.38616 | -47.03878 | 2025-09-21 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08a1e8bb-9d93-3c5f-8e29-76de374bca1a | -10.28514 | -46.07248 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6d01728-de20-3e0c-98d2-027ab301021c | -6.89971 | -44.74425 | 2025-09-21 04:36:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 451a2ab6-10d1-3a4d-8a27-67b040538611 | -7.7183 | -44.45624 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccb8d67c-b348-328a-8004-4dc49fedd50b | -12.07639 | -44.81324 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87c0b834-e7e0-3171-b020-7c02908754c5 | -6.22775 | -44.65995 | 2025-09-21 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c472b87e-d2eb-3f3f-91c4-765b5a252b6c | -11.25836 | -49.84288 | 2025-09-21 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa35bc9e-91fa-38ba-9e63-7b372ce26007 | -7.83021 | -45.62774 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8062e69d-f61c-344c-8dad-7e4f13b5281b | -7.93709 | -44.10029 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 90e858a4-e4da-3027-b307-ba0462234da6 | -6.84811 | -44.14811 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a6b0048-69fd-32f1-8b36-c4f36c339f87 | -9.7747 | -47.17715 | 2025-09-21 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87db5e7b-8f4a-330e-b6d6-c7069fd42174 | -11.77919 | -43.7614 | 2025-09-21 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 66bafb6f-dc23-36b8-9042-cb1796801528 | -8.28241 | -41.6807 | 2025-09-21 04:36:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67846d2e-584a-3214-a972-5e44b4ba17fb | -11.10924 | -49.67935 | 2025-09-21 04:36:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e5de861-b93c-31dc-a19a-970e03cc115b | -10.78559 | -47.33856 | 2025-09-21 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 111a719b-43cd-3f2d-88f3-4dc9bedd79d0 | -10.34925 | -47.88923 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef57db95-4032-3cfc-93b9-47523e57809b | -6.59311 | -43.58292 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6db5c142-769f-3b1f-bd9d-24c809f9ea51 | -10.35986 | -47.88722 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c62ea9c0-99c1-3cd3-8b41-ba73f59f691a | -6.94441 | -44.74484 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c13f671-825b-3115-94e5-6cbcf31453fd | -10.3456 | -45.22879 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 471eb9f3-a48d-3e69-aa8c-590e0bf0f778 | -7.72068 | -44.46573 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fba19f6c-dc4d-3341-87d2-29d1ee656488 | -7.46325 | -42.63762 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ac676ec-572a-3d73-9903-172ced098ce2 | -11.27739 | -47.40641 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53374264-2ce9-37ea-b659-d730d44aca2c | -7.92874 | -44.10386 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2be82c1c-9129-38d2-b53b-628384d20bf9 | -11.30193 | -47.51963 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed5327ce-2f61-3c24-88c6-0d41651fb03c | -12.07558 | -44.8476 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7947a47a-7be8-3f72-9c15-17f61b990275 | -12.08469 | -44.8029 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a9a823-994e-3f35-982c-1acef93d7932 | -6.69408 | -44.09681 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47edbc36-2fe6-3702-bff7-b2c7c0849380 | -10.41958 | -47.85654 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a18ab149-c979-34ff-8551-556bb227a01d | -10.3526 | -47.88976 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 103642e5-a448-38f8-9437-f6218649afb8 | -8.84103 | -43.00499 | 2025-09-21 04:36:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e958bf18-a50e-31e8-bbe1-3dcf8727e128 | -11.31492 | -47.50291 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e3179c15-14e9-3bf3-823e-4e99b4f20da7 | -7.35036 | -44.54639 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd8aeee0-0ca1-3807-94df-a060fbf263eb | -11.42984 | -47.31882 | 2025-09-21 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 935aad7a-1808-3bf2-b7fe-0784d81adff7 | -9.17266 | -44.61967 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21d4bf8d-fef9-3bae-91a9-7768604e999a | -12.35232 | -43.75476 | 2025-09-21 04:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bed2723c-240c-35f4-be4e-527c33b1e16e | -12.07771 | -44.85095 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 183fd30a-d623-3e35-b6f6-794bfcb60af1 | -8.3512 | -44.70924 | 2025-09-21 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
