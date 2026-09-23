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
| 5e735371-5b8c-3b9d-9f82-0f6b1655989d | -3.465 | -59.551998 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3acf9e-3432-3a74-87de-c0c98b7a3c6f | -3.2795 | -57.853901 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abdc5a5b-796a-3fb9-a00c-6bfdf0dc7acb | -3.8516 | -58.657799 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0fcf9a5-3d24-3ac7-b800-a8a98aa8457c | -9.8592 | -48.308899 | 2026-09-23 00:36:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63bf0f06-8b49-324f-9067-18e43f66493f | 2.7702 | -60.222698 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c79d9732-7918-3c8d-af19-274441f5eca5 | -9.0062 | -57.123199 | 2026-09-23 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0849831a-c500-308a-99d3-888bc12f03d2 | -2.9232 | -57.781898 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6a0916-0b88-3611-9679-aa7ee616e861 | -9.6835 | -54.3176 | 2026-09-23 00:36:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1b400d3-031c-3694-aa5c-a3b4a781ed00 | -5.1609 | -60.290798 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5de66f-5ce6-36cf-95bc-e799c726558c | -6.8133 | -59.444199 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 150777cb-7e65-3c8b-abc1-d3160944f605 | -3.0399 | -54.396301 | 2026-09-23 00:36:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f696f8-6459-32d8-915c-e88dbff59126 | -3.5277 | -59.602001 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1892fbb-4f0d-3639-a20e-80200cc7dbe3 | -2.762 | -57.023102 | 2026-09-23 00:36:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee8edcf-fa04-3f83-8995-c4ca7c31a946 | -3.4911 | -59.162601 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba1ffcd7-d080-3d74-9eab-c704a59891be | -6.779 | -48.680199 | 2026-09-23 00:36:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2f35840b-b5e5-3067-a66a-ad2f6a96cebd | -3.4864 | -59.555199 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7b7db7-5055-390d-b048-2bf3beacbd34 | -3.5375 | -59.5998 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3477c99d-b3aa-310d-a5fd-1aac372dda7e | -2.9103 | -57.770401 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd0eae4-92bd-31fd-a6c9-4c37180f0d39 | -6.6866 | -55.058498 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83068e7-bcd8-3b2f-a766-09f03f8d10d1 | -3.0418 | -54.4044 | 2026-09-23 00:36:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 676d6049-5ccc-32f8-8f15-afdd6a42d1be | -6.4317 | -55.613701 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aae13df2-1e18-3e75-89f8-9cb38da33537 | -6.4686 | -59.9804 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e19b82e2-c8b6-3007-991d-7ab829376d06 | -4.3837 | -60.956501 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10344475-4c16-3c67-b52c-6ebef3ea0bbd | -8.3005 | -54.764999 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36169277-f722-3350-96b2-d21c579e7bc4 | -3.5908 | -59.056198 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30e795b9-b93b-3f87-b007-cdc5fb5ab1dd | -8.5863 | -54.616299 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5080a150-df13-3d24-bb10-e5ec6084ceb4 | -3.1389 | -60.624901 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5002d4ea-9a48-3f41-8dc1-ce7578c8a8be | -3.9972 | -52.075699 | 2026-09-23 00:36:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56ac4815-4e51-3675-9146-6f505245d96a | -3.6836 | -60.532398 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00a10f05-6ae9-37d3-b3be-c589bc9421fe | -12.7637 | -50.8895 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 491008f9-d1dd-3fae-8769-734ef43c662d | -3.6071 | -60.557999 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44002e25-a101-3f68-9962-c4d739b360fd | -3.1578 | -57.6796 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82977463-46a7-340e-a2e7-c71bec653e49 | -2.9201 | -57.7682 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93f73b3b-afb6-3195-97e1-6d4a23e89c94 | -3.4888 | -60.211399 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44e078b-2794-398b-a570-e7ef86f8c7c8 | -6.7277 | -59.428902 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 944ffba1-58f4-357d-8582-e1234130c470 | -8.9359 | -50.906799 | 2026-09-23 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf227b5-c019-37e6-8ed4-794564540657 | -6.3728 | -55.264599 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d08523e9-b504-3c32-88db-aad03e90f22f | -11.4499 | -47.372898 | 2026-09-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2267181-0466-3cdd-aa18-6daaa52d0ddd | -5.8875 | -52.098499 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 516699d5-2f75-302e-b827-4492870ed0aa | -3.6855 | -60.540901 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0bc7c5-11c0-3ac9-9cea-b9999a352e1b | -3.4633 | -59.544399 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae6a860d-de70-3193-a2ef-0f64c14b3e16 | -6.3025 | -59.971901 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69607361-316c-32ca-a1bb-c75b175f92a1 | -7.5524 | -55.011101 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0537cc-6872-3a00-a1c5-7b4d65012404 | -3.7716 | -59.588501 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72cb9fb8-86f6-3f54-898f-3c7240436f0e | -4.0521 | -56.302299 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef7981a-b7be-3891-b775-64a6ab6de593 | -3.6923 | -58.9118 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa8e44b-6abf-39d8-8367-9fea67aa1f61 | -4.8553 | -55.844398 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61dda460-0097-37ac-b47b-ddf7122bde94 | -9.3272 | -60.0672 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91ac7b9a-f83e-348a-b88e-6099aea6ac16 | -10.1416 | -58.747898 | 2026-09-23 00:36:00 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9faa2011-b46e-34a9-b62a-a99940a6f141 | -7.0249 | -44.660801 | 2026-09-23 00:36:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea852ce7-e3a6-30b2-a92a-dea5afddfc0e | -3.0415 | -61.2486 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5015572c-84c7-3eb2-b4bc-24fff2bbda80 | -9.2401 | -59.5639 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e081b3d0-528e-3a18-895e-e7a0daad3689 | -6.6752 | -55.053501 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf49535-a6a4-3349-a23b-ae36cfc85e09 | -16.632401 | -42.3437 | 2026-09-23 00:36:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1736aa0c-8e06-3830-8e9a-5b1c0730873d | -5.7536 | -45.082401 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50805d73-194c-3e32-9613-2978f7772cdb | -3.6791 | -60.604401 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0ed126f-8e20-31ae-8495-392f772be5d4 | -6.084 | -57.682899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e8aa57-3df1-3ef0-a310-a292355238f9 | -3.4615 | -58.387901 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24085eae-e8b8-3537-83e4-26541bfd30e0 | -3.609 | -60.566399 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb3ed2b3-9869-3757-8f5b-e69145416aea | -3.6571 | -54.2565 | 2026-09-23 00:36:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b868f4a8-3365-3867-9c00-c6210992f3ec | -10.3842 | -54.405102 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 220d0c38-d37d-349a-a0f7-076c9c1fda83 | -9.5313 | -45.359501 | 2026-09-23 00:36:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc090a92-a9e6-3945-9994-e2087ed9b3cc | -2.9767 | -57.1973 | 2026-09-23 00:36:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf4add2-c47a-3673-9936-bfa1a96edb52 | -2.7866 | -59.8773 | 2026-09-23 00:36:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85ee773f-409e-3cf4-b5fc-d0b6abca645c | -12.8073 | -50.8988 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6beed370-54f2-309d-b8d5-c48caff541bc | 2.78 | -60.224899 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1913cfb9-2197-3476-8f79-7509954aa1ed | -4.2792 | -56.258701 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5fc114-1eed-371f-87ef-2180e20470f8 | -6.667 | -55.062901 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c980f8a-fbaf-3435-8874-65e141cb6a35 | -10.4492 | -51.277401 | 2026-09-23 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55da609b-751c-359f-9f06-89fdea63aabd | -6.5908 | -51.322201 | 2026-09-23 00:36:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44852dd1-6469-32a2-96b0-2c90ecb7dd75 | -3.0709 | -59.124802 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a739b6d7-39fb-351b-9917-172e8e7ff3df | -1.2089 | -54.542702 | 2026-09-23 00:36:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c26769-bd7e-35a2-953f-af26bdd39b16 | -3.4667 | -59.559502 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 729e01d8-19c9-3ec8-b2d8-bded40861b38 | -4.2883 | -49.127399 | 2026-09-23 00:36:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a5e106-80a0-3759-a6b2-d1884fd9b67d | -3.1495 | -57.688702 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb2084eb-a7c8-31c0-b6cd-a7f1e526b2a2 | -12.8193 | -50.9058 | 2026-09-23 00:36:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 89c8e903-e85e-3973-bcae-114ea5744ff5 | -2.9588 | -54.087299 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c8a4c4-d33f-3f44-8d94-8212c081addc | -6.7376 | -59.426701 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2a66ada-0e82-3e4d-8601-7efbdca4660d | -1.9076 | -58.258801 | 2026-09-23 00:36:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7deda596-bc15-3e6f-83c5-9c9924ef8a94 | -2.933 | -57.7798 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78641319-f0a4-3ab4-8418-4c553d256e3e | -7.0918 | -52.7491 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2bac5e2-7de0-337a-876a-7b2ce0ed0dd8 | -8.2436 | -55.239201 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3a62fb-2500-34ae-930a-e3b31daa20b8 | -3.4586 | -59.247101 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8529d005-371d-3cad-9f21-5ea073f976b6 | -6.5774 | -51.483299 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67c8858-ee92-390e-8a22-cf289e1b9889 | -10.8516 | -56.208599 | 2026-09-23 00:36:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a436113-2120-3955-8915-455d595cd13c | -6.6834 | -55.044201 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f37eb70a-6d95-3483-9a97-c7f9e068b62c | -4.2683 | -55.440201 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83d206a-5422-30cf-9675-a205ad115651 | -3.8868 | -51.955399 | 2026-09-23 00:36:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1b0618-b3c8-35fa-bf3d-64bfa76e70bb | -3.4439 | -58.172199 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b468a832-043c-3e3d-a2b0-6c3d8b5b7a95 | -3.4944 | -59.177299 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bddce18a-3fa1-3716-acc7-b149a558540a | -4.1659 | -60.760899 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a374dc0c-d87f-330a-bed0-f721dc8f8bb2 | -6.6736 | -55.046398 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0485b3-fec6-3a8a-bd8c-81fc554e56f2 | -10.6149 | -53.970798 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb8f720b-8ec3-3b7c-adb0-917d70fbc453 | -8.2809 | -54.769501 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7720f9ca-37dc-390c-8c23-d265aed3b6b4 | -4.667 | -55.9235 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a125b57-ebff-3a5e-bc03-24eaa636e630 | -6.639 | -55.256401 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67948c48-65b8-3ee0-816f-87311399c8c5 | -12.7592 | -50.870499 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13a157d3-dddf-3dd1-a912-6934ad6b3894 | -3.8543 | -58.8078 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2c843a-deb4-35a3-942a-63051a842b96 | -3.681 | -60.6129 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7919663b-ce75-3249-920b-48c02e325b92 | -8.2058 | -54.7113 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
