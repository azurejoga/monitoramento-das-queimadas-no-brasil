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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67335185-5b7a-36b5-9c51-35ce43eeb0c3 | 2.89281 | -60.27476 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7295c6b-f904-3bc4-a848-9ae850e2307c | 1.62713 | -56.04268 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 82cf16d1-3b0c-3240-846b-be2121f56f1a | -3.22996 | -54.31979 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb2d9f5-e37c-3d65-bce0-93f42e7f4f23 | -1.83824 | -54.72316 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b17ee1cf-9c4b-3efb-9706-b6468f3f2aa1 | -2.14647 | -53.7118 | 2026-09-26 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc9f276-7370-30b2-b651-2950de22bb56 | -2.99252 | -50.47111 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8448243e-3a20-3647-936e-abe08a5c3ae7 | -2.47203 | -57.9358 | 2026-09-26 05:46:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44825e44-ab13-3d4a-8643-d646f95b8295 | -2.57493 | -54.74321 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 259a7a7a-2b9c-391f-ae61-02be5020c17e | -3.27179 | -50.1408 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7425c25f-82b4-3bd7-bc7f-d20563ad0570 | -2.15485 | -51.9797 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 323c65f7-83b8-30aa-80bb-e7dfea7fb23c | -3.26995 | -50.14089 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af7ea124-56b6-3a25-a19b-b0fac792c942 | -1.69286 | -55.55866 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f1b9bd74-0610-3941-a9d9-03549bea753b | -1.69498 | -55.56239 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d5304000-439c-334c-9460-00bc4ec191a8 | -1.14106 | -54.08618 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 50eb9266-3114-3e78-b30c-6ce7f028e985 | -3.80438 | -51.02567 | 2026-09-26 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16515cc4-d76d-33e2-8482-fc21fe4d7acf | -2.99527 | -50.46909 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a88abae1-9498-3362-98cb-7fb87930293c | -2.06805 | -56.87092 | 2026-09-26 05:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 531cd6c8-af47-3382-9c60-57427e41a32b | -1.84402 | -54.71838 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3ab2a8b9-5513-3757-9fa6-d06cfe4eaf36 | -2.90053 | -54.09485 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1276f60c-55d2-3d53-8924-c67cba2fe690 | -1.35657 | -55.38909 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22beacfe-7424-3de4-b80c-dde28c99f9c7 | -2.90019 | -54.09793 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 586f12b5-cb2b-3367-9fba-738169558c92 | 2.71407 | -60.68407 | 2026-09-26 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e94f250a-2355-35cb-a028-1da148e6d26e | -1.84319 | -54.72392 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3b8aa65d-923e-3245-bf0c-1a968d528727 | 1.62286 | -56.04337 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7fc27cb-3fc0-30b2-bd90-fce9f2a5e81c | 1.57896 | -56.05847 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b5f17b-4434-39a8-a821-1262afe4fea2 | -3.71606 | -54.64622 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56b80634-3bc8-3828-9338-a8ca6cf245e4 | -3.8051 | -51.02076 | 2026-09-26 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 561dcc59-d7d8-330c-af83-63b0e1f46439 | -2.84062 | -51.36081 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1eb795a-06dd-3be3-9d6f-002ccf3f0d11 | -2.90579 | -54.09563 | 2026-09-26 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 474315d3-8faa-3537-b19f-cb48c0b78d01 | -1.68961 | -55.56623 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 834a72e5-a6ba-3f9a-a188-26efc56f70dc | -2.6559 | -56.45075 | 2026-09-26 05:46:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9b061038-872d-3c15-92f5-2e0ba280fc04 | -2.97829 | -54.14851 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78c2eb9e-fb3e-36cc-8aa3-724b617676ce | -1.1406 | -54.08915 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc21d0d9-a2be-3c01-adcb-5331c1e56b75 | -3.20333 | -53.41209 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4045eca-9ba8-3e68-97a4-9bd5ccdecf7e | -3.72074 | -54.64994 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a530c44f-3019-30cf-9cd2-0e580266d951 | -1.34372 | -55.47147 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acf721a7-1356-3561-92aa-f68511db2c55 | -2.40997 | -56.4271 | 2026-09-26 05:46:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3045c576-5e62-3095-aa76-8b06c5184421 | -1.21886 | -54.56667 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70f121ae-b05b-3a5f-b07b-af1cfcc2b0fa | 2.71797 | -60.68704 | 2026-09-26 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 244797ef-63bf-3116-8fd4-d76d636ee548 | -1.22005 | -54.56149 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a47fdfe-dcf6-32b1-95a8-85e5cb96d5f8 | -1.84292 | -54.7231 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| aaea7ab4-5541-30bd-9135-ab076c2cce2c | -2.15315 | -51.97318 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ebd9d46-10bb-3183-bd83-80ce30164757 | -1.14572 | -54.08988 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0dcfde0c-ebd5-3e58-a1f6-429928081ae3 | -2.66792 | -56.46151 | 2026-09-26 05:46:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9fedb68-72d8-3748-83d6-cccb575cf637 | -1.32116 | -55.67645 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb6c1fe-91e7-3baa-b0c7-8843dd874740 | -3.00102 | -50.47593 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37c1b439-ed7b-3051-97d1-96f59cb2cbbb | 2.05143 | -50.97252 | 2026-09-26 05:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78f0bf3a-61a3-3056-a91b-7865ce9ebd01 | -2.97779 | -54.1517 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c84f27c-753f-319f-8797-38ba42893d79 | -2.57491 | -54.74246 | 2026-09-26 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a52c881-18f7-3749-afac-ffc9e2c28038 | -1.14525 | -54.09286 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbaf3d40-6a52-39c3-ad9c-026c59ff04c0 | -3.30798 | -54.68752 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc242412-ba88-3462-aa67-f5062a95379f | -1.68497 | -55.56538 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e428d7eb-b776-3548-93d6-1ca9d82d37da | -3.20375 | -53.40735 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00d35157-0dd9-30b0-abc7-903da4174ccb | 1.47857 | -56.02412 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09bcc9b3-9f6f-314b-a2a3-383cab18776d | -3.71474 | -54.6551 | 2026-09-26 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94b33bcb-2ed1-3217-8a80-ce9594d8fb15 | -2.94539 | -57.71749 | 2026-09-26 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0127a435-0097-3cab-affd-11a21206a7c5 | -1.14989 | -54.09661 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 453bd349-b5c1-33fe-9c54-292f1182b21a | 2.93578 | -61.26908 | 2026-09-26 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ec78a9e-7b1f-3447-91af-db0303b41111 | -3.30292 | -54.68665 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e56336f2-a2f7-30b1-a192-ae470e707166 | -3.79864 | -51.0195 | 2026-09-26 05:46:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7340945-8ba5-34da-a0e5-f85a5685d8e7 | -3.87683 | -52.28306 | 2026-09-26 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65af2bd4-b8e0-30b8-8f48-d2f86b190652 | 2.93523 | -61.26562 | 2026-09-26 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd33bf7b-b674-3acb-a3e5-2e88758bfdd1 | -3.30754 | -54.69042 | 2026-09-26 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a54be5e-957b-35dd-9e38-376875be74d7 | -2.47149 | -57.93927 | 2026-09-26 05:46:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0076451-afe0-35cc-ac52-43f69635481b | 2.04614 | -50.97773 | 2026-09-26 05:46:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067edb1f-a29e-3acd-81ce-0fdc94fadcfb | -1.13919 | -54.09809 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9f095cd-ed74-3885-8227-6d7a56fdfc05 | -1.83797 | -54.72236 | 2026-09-26 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| dea3184d-698b-39e3-8807-cc436c59598c | -1.14894 | -54.10263 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70df3058-2497-3913-b6f4-ea576cbb46ff | -2.1523 | -53.70936 | 2026-09-26 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d989caf-7797-3c3d-9e8d-590f88f54976 | -2.99911 | -50.47246 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d45280a5-6378-3870-95c2-9d08090a443b | -2.14953 | -51.97437 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1754f04a-2c28-379d-a7b0-c518a4fad624 | -3.27092 | -50.14681 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 984c6d24-5b0f-3a0d-a6d5-b2a8713bb175 | 2.62312 | -50.89375 | 2026-09-26 05:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d95f52-ed04-394e-988d-29edc0468364 | -1.68572 | -55.56063 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9bdffe3-87e5-3925-8041-65e04a49bc3d | 1.30164 | -50.83249 | 2026-09-26 05:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d1d3a3b-f09c-3642-ae49-1afcfd835487 | 1.62351 | -56.04734 | 2026-09-26 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39b0c998-a5fe-32ad-a5f7-cb52e21932c5 | 2.8861 | -60.29778 | 2026-09-26 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0664b5a-8646-394e-b334-338e64458eb4 | -1.33832 | -55.47549 | 2026-09-26 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46086d43-0195-363f-b596-228081d94469 | -2.98784 | -50.47332 | 2026-09-26 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be44887-b8b4-3ec4-8524-5f8a6e6c88fd | -2.15246 | -51.97756 | 2026-09-26 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8dc8661-e8d2-3b47-93ef-4910c9e7d358 | -3.20928 | -53.40822 | 2026-09-26 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5bc292-8710-3144-b38e-7cad1f3a6fb8 | -1.14013 | -54.09212 | 2026-09-26 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8a53fb0-41f3-3ec0-bfc0-d7557590ac4a | -3.87082 | -52.28223 | 2026-09-26 05:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38c61bc8-e173-398f-beb7-1040bf774fe5 | -8.24265 | -54.6661 | 2026-09-26 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4e475a0-c485-3930-b9e6-3f6d8e7cc249 | -9.63515 | -55.13369 | 2026-09-26 05:48:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c35ff41a-9027-32af-ad1d-49b668f07d63 | -9.64054 | -55.13457 | 2026-09-26 05:48:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f3d9f1e-cf1f-31eb-9f22-c0f4b912d58f | -7.12482 | -63.10723 | 2026-09-26 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7112b5-0deb-3bfa-9898-f41be6e23e1b | -9.50821 | -54.65879 | 2026-09-26 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 664b03c9-3dd6-3281-a29a-e263e5cd4dcf | -9.64009 | -55.13797 | 2026-09-26 05:48:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d87786f7-9333-3e30-bb39-f3d4e8fba687 | -8.24763 | -54.67036 | 2026-09-26 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98c856c9-c565-3eed-9e49-51297f604664 | -9.51378 | -54.65954 | 2026-09-26 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2777a859-00f2-35fe-a4c2-0495bbcb6b5e | -7.26295 | -72.69412 | 2026-09-26 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55df3d83-b740-30b4-8125-72b34e38fa06 | -7.26353 | -72.69096 | 2026-09-26 05:48:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 070ec7f8-e63f-3ccc-bbd1-9ff1d753d329 | -4.97624 | -56.1925 | 2026-09-26 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58b19c12-b5fe-31eb-bd1d-7efc759ed10b | -12.02438 | -50.65033 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d59defda-8f16-3415-b2a7-51e45ac5b6b0 | -12.03172 | -50.6512 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1569885-bfc0-3e62-a6e1-3086c380bb9a | -17.04126 | -56.5853 | 2026-09-26 05:50:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 50db2691-261a-3d57-8882-412804e3808e | -12.89889 | -61.71656 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad2dcd5-15b9-32c7-a50b-abcc846aa79b | -11.95435 | -50.67451 | 2026-09-26 05:50:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14c3214a-72cb-38f3-bdcb-fd30754999d7 | -11.76497 | -50.63744 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README29.md)
