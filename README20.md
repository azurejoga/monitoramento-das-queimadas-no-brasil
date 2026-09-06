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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a136ff8-4019-3966-bb41-503867cfe58a | -5.57044 | -60.1613 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51f64f1f-0188-3c02-9afb-9d62178a6b35 | -8.98363 | -44.4121 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75795669-f0ef-3c11-95df-5e58f25b892a | -3.76281 | -61.76484 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c549e707-97dd-344c-bd88-8679b6cf4231 | -5.84921 | -52.04699 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87f0224f-5c62-3ec1-8ef4-52868792131d | -5.37017 | -56.03589 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 42e31838-a758-308b-8e45-26a8ed260fb7 | -6.589 | -58.60231 | 2026-09-06 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77b011e1-2b4e-3937-8bca-ad5e0822c18f | -7.34287 | -55.21421 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0be1b664-c604-3ac7-b0b7-4df93dfe51e7 | -3.76359 | -61.7602 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a01ba03d-fb96-367d-9f29-5e07fd3ae5ae | -7.90175 | -47.69604 | 2026-09-06 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4527d3d9-518c-3430-9709-51b16d41d453 | -3.79619 | -55.87936 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d96fc13c-8523-3328-b9b0-1efb70febaac | -5.84977 | -52.04347 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5cac0dd-79e3-36f1-baf8-48fa61ca982f | -5.35921 | -56.02679 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c78ece6-84fa-35fc-91cc-a6b709234244 | -11.27605 | -45.70205 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14607a8e-f137-3ff7-9812-53a7f4bee58a | -5.16844 | -56.04684 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23faa427-fe90-32d7-95cf-e4592843505e | -5.30261 | -55.86975 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0a29ce-885c-38f3-8353-7ea2a52f07b4 | -3.37744 | -59.41896 | 2026-09-06 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa36bc6-d227-3145-8dd7-8b79cf912766 | -6.51762 | -58.29461 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db42ba90-5bb5-302e-b266-152d896889d2 | -6.35683 | -47.27582 | 2026-09-06 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c247ab8-ad2a-385c-b160-2b406ffaf6d9 | -5.34827 | -56.01766 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e99c1cb9-0f83-3a97-84ea-c4ab46bd7d97 | -8.50389 | -54.65198 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94fb575e-cb4d-3300-99fb-e09b06c28997 | -5.30614 | -56.02176 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b868139-40fb-3478-a79b-09ebe61e4333 | -2.9397 | -57.89521 | 2026-09-06 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2164d4fd-2720-320b-96c0-6c1359b63814 | -8.98429 | -44.40698 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8991eba-65f9-3292-9176-74352c320376 | -7.09654 | -56.51397 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c09d65d5-e8be-38a8-8763-86ce13225b87 | -8.94839 | -44.4106 | 2026-09-06 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d663a9b7-64ac-3f2c-9475-ef7b89ab8faf | -3.76436 | -61.7556 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a4dc667-7c2f-3241-aa05-80e90372020a | -6.87695 | -55.61126 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 711d50e6-53ec-370f-af7f-4e1c88992895 | -5.30205 | -55.86212 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dde6542b-ff27-330a-8b1c-d644d2d60d56 | -2.73713 | -54.15496 | 2026-09-06 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d22e7574-ba0a-34cd-9dec-a4c7455b0d17 | -5.77296 | -45.07167 | 2026-09-06 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d6ba4f-24a3-3840-93a8-e9984c6110c0 | -6.06188 | -57.80548 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96434389-e9dd-338a-a427-64b55f931ab7 | -4.8172 | -49.3887 | 2026-09-06 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c9b9dcbc-e8be-37d1-be27-012a5203e9e6 | -5.30269 | -56.01756 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c37284a7-0968-3a74-b05c-461f96c4e811 | -4.92247 | -55.81291 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 753fadf9-2fb6-398c-a432-4742357ce89a | -5.145 | -55.95745 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca630407-2af8-37cc-a5db-7d11650ea4e8 | -9.57393 | -40.36084 | 2026-09-06 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| e92c9561-68c9-35f8-aae1-6c33f042a78b | -5.35286 | -56.04032 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 400de035-2d8f-3fe4-8615-ace54b15ce9d | -6.88046 | -41.04264 | 2026-09-06 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bfc7f14-6d25-3e30-878f-9edb85ed5927 | -7.10869 | -56.51607 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d02072c2-8eec-3822-a021-d9be507942cd | -6.0013 | -57.78086 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07681be9-e92b-3f94-814a-2155cf2ccecb | -11.3331 | -45.06549 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d367bf06-96ca-31a2-8e53-0ddf14648d7b | -3.37797 | -59.41574 | 2026-09-06 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2237c38e-144d-32c8-aff1-e18650d5be27 | -5.30791 | -56.01112 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ea8b91-10b9-3746-b7c5-40795405febe | -3.33629 | -54.17605 | 2026-09-06 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15a46714-5b23-31f4-ab80-fbf26e78b633 | -7.96692 | -54.90779 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51571af7-0bde-3ccd-82f2-54f075fe6c13 | -10.59574 | -47.26098 | 2026-09-06 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71cb3c08-b106-3db4-b87b-48dc1968b434 | -5.30319 | -55.86629 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dc6341e-e4dc-3055-9e8a-4aa56d41a5ba | -3.77115 | -61.75903 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed4c9793-f6bf-3c25-a9bd-9455e8b7c067 | -5.33903 | -56.02345 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d879d7b-90ac-3952-9113-c84db73628ed | -6.06412 | -57.79189 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| af18de4f-5043-3679-9630-84264a7d0ee3 | -3.76346 | -61.76726 | 2026-09-06 04:46:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d1a2a6-413d-3b66-863e-52609d7bd90f | -5.6507 | -60.23706 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e643aa9-08c5-314e-9385-d3e6a9f3e968 | -5.85206 | -60.2566 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fbec95d-cd08-3b3d-9bfe-3707a4e9f8bb | -5.65128 | -60.23363 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fa8e2cc-7d1c-3eb1-859f-bc645eebd545 | -6.87231 | -55.61538 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b01b1b76-d0f1-37a8-a4f0-a217fb8276cb | -11.27986 | -45.70738 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fc22e44-5015-30e1-b1dc-d197b30e9a27 | -7.27355 | -55.1472 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6f872a7-20ce-3a8f-9ced-463ad9aa2b1c | -5.77126 | -45.07352 | 2026-09-06 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 731fd68d-490d-37d0-8525-e736d061b45f | -5.25595 | -59.98257 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2323d893-a0c8-3e7d-ac9a-80f05c8fca51 | -5.13412 | -56.27648 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d1fbe8d3-8d35-3179-9346-328589a2d3a3 | -6.87084 | -55.61182 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a458d623-3456-3826-abd8-92fa5f647208 | -3.69127 | -49.53203 | 2026-09-06 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 250075a6-5364-3fbb-876c-93cc4cc8bb2e | -4.45368 | -46.13822 | 2026-09-06 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dfbffd55-bb17-35ce-94bc-d8f9e8356f9f | -4.34854 | -56.28912 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45c25d0c-dd6b-3347-bd95-b5445aa24268 | -6.06713 | -57.80163 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48e325b0-8f49-3862-a211-3c0f7d51aea8 | -3.62461 | -54.60448 | 2026-09-06 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e00e5ac-50f1-383a-b717-0e2f94349de3 | -11.32785 | -45.06941 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 44b73034-d3b1-36dd-aaff-b6d811017fab | -6.87615 | -55.61603 | 2026-09-06 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1d903397-9d2b-3d75-af5b-14cabcc48dc6 | -6.25296 | -46.66788 | 2026-09-06 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b50d347e-4ab0-3b2d-b6df-e9b74dcf1fd7 | -11.29354 | -45.69799 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35f4bdf6-b7d0-35df-9754-8be49baffaa4 | -5.85065 | -60.25381 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9b52b95-fdf6-36ab-af33-a9f27e2fadfc | -4.671 | -55.6326 | 2026-09-06 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b6a6cbb-928b-302b-bcbe-c9ec071d8e22 | -5.50544 | -44.02477 | 2026-09-06 04:46:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73f8011d-ac23-3a40-ae27-9d0f983c5471 | -5.28544 | -60.12717 | 2026-09-06 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a1a5da-30fd-398f-a36f-5cb861f228d2 | -5.17008 | -56.06189 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44844c47-74a3-3892-976b-499f15527789 | -5.85532 | -52.05158 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1585b82-a935-3805-a915-624a1b75f7db | -11.29372 | -45.11351 | 2026-09-06 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a762567c-752a-3e4b-b9bb-e6fab7e708f5 | -6.05747 | -57.78909 | 2026-09-06 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 270f2e75-5975-3bff-9ff7-7981b12fdcf7 | -4.46942 | -55.09064 | 2026-09-06 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe133417-9487-3695-bbf6-eb89767e4570 | -3.15572 | -50.8284 | 2026-09-06 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c6b4e35-8cc8-36aa-9a2d-555d263b1151 | -5.36439 | -56.02037 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 048c7e4d-5a3f-3610-99a9-3d552265e018 | -5.36728 | -56.02813 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 52a5ada9-4081-366d-83de-c441bcf7f21c | -6.46393 | -55.07996 | 2026-09-06 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03319d9a-c8c8-3341-8e6a-a5fe0665ab5e | -3.94077 | -48.44517 | 2026-09-06 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6fb1e97-2d89-3ff6-bfb6-d51ba5f33011 | -5.14789 | -55.96518 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fff93e74-5e09-3fbd-bfea-32866342ad54 | -5.33961 | -56.0199 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87e3c5dd-9125-3ee8-93af-d4e5661a3108 | -6.87993 | -41.04669 | 2026-09-06 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 387f7b4f-48c9-3bbf-8755-445f3b81b895 | -5.17414 | -56.06253 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 893dcdef-58fd-3c9c-847c-515e3e5a2189 | -7.6748 | -46.0508 | 2026-09-06 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92cc337a-b96f-3c8c-9d1b-b908b4591731 | -3.71608 | -51.13933 | 2026-09-06 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2fd3158-ebc9-34fd-9d7c-8513a49af281 | -3.38322 | -59.41655 | 2026-09-06 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c578f9b4-0801-3caa-95e5-e3a412c463cf | -6.27046 | -43.2711 | 2026-09-06 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e6d3f55-4011-39ba-ae60-7b5eb9b4cd91 | -5.30328 | -56.01401 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 345d009b-9870-39ca-8188-15d1e219bd51 | -4.45759 | -46.13892 | 2026-09-06 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d5a6ce8c-cedb-3b6b-bdc6-b6834f4890af | -4.36236 | -47.77573 | 2026-09-06 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 273ce6d8-b7ae-3766-9f6d-c357efc07fbc | -5.16438 | -56.0462 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2ae9d7-1e35-3d7d-94ea-8bc041ca90b4 | -3.83372 | -60.769 | 2026-09-06 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3d2a8fd-c7b9-3e86-bfa7-2bdad5338374 | -5.14615 | -55.9504 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4e70d41-90b0-367c-9c56-1ecc6a517839 | -4.06572 | -55.38964 | 2026-09-06 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71806f9c-9a4a-3d22-b463-0b88eb0e1bfa | -5.34537 | -56.03539 | 2026-09-06 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
