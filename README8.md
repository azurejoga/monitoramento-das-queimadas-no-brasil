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
| 55c426fa-5f01-3dd9-ad5c-fd3eb3cd3870 | -6.96377 | -43.57842 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e9b6e2d0-41c7-30e3-8c8e-ad63b96b5546 | -5.551 | -49.06808 | 2025-08-19 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 2331ca6d-3508-3feb-92a4-3928d22f13aa | -9.1812 | -59.63031 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| aca1873b-3652-3d26-bb2f-d5fee4dfb5b9 | -5.87083 | -48.12634 | 2025-08-19 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| bf994b22-46ad-3900-96ea-6c1d4076694e | -3.45057 | -48.97141 | 2025-08-19 00:50:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 56ff9504-d62f-3d80-af4a-726626a98d56 | -8.96579 | -60.49593 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1afb65ba-94a1-3247-8f21-09320ec3ca56 | -6.95327 | -43.61083 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 11f05ceb-e76b-35a4-8903-77b30a3b2473 | -6.63182 | -55.28263 | 2025-08-19 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d9a09ce-78cd-3a20-b874-6982d3573225 | -10.60234 | -51.1742 | 2025-08-19 00:50:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da5fe21a-8609-3b66-acf9-f4211be4ca41 | -8.77155 | -50.02407 | 2025-08-19 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 08672583-a14c-30ff-b1c4-f207e944cf20 | -11.57771 | -44.85806 | 2025-08-19 00:50:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f8f8f2f7-43b2-31a7-84b9-7bbea0df04fb | -5.55276 | -49.07994 | 2025-08-19 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 38b1e9c3-5cf8-3f74-9b4c-83d4268f52b6 | -10.52521 | -50.36333 | 2025-08-19 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70b331d8-f3ae-3e31-8c26-0b50bdd8f4a1 | -10.45805 | -48.80925 | 2025-08-19 00:50:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 280d2f1c-b994-33fd-bfab-80fedd118898 | -13.17684 | -54.96082 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 36ffd2c9-36fc-37ad-9c9a-fd32bf0dc4e7 | -6.94135 | -43.61802 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.0 |
| bb1214b4-9ac0-3c4e-8d7f-8ad8189f4f82 | -7.12325 | -50.42824 | 2025-08-19 00:50:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a05b1e7-cc7c-321e-aac3-122a3da1833f | -7.25299 | -50.16328 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 98ac0a85-4697-3c06-8c0a-ac19f26c3b9e | -5.79298 | -43.62427 | 2025-08-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 72efceb3-f4a9-39cc-8ccf-2807532828bb | -10.60359 | -51.18317 | 2025-08-19 00:50:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 284ce054-7f99-38f8-9e5e-6c0c69c8d020 | -5.54149 | -49.06313 | 2025-08-19 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 8a8f1f19-3a45-32d6-ab2d-d578a15ea2a4 | -6.54947 | -49.52134 | 2025-08-19 00:50:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b62fb68f-9da8-3793-992f-830941264ceb | -11.73641 | -58.32143 | 2025-08-19 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| c0d1879d-4196-3dff-b400-ed3c4587a224 | -9.51273 | -60.54328 | 2025-08-19 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0227301a-0829-3638-a2d3-7144990f506f | -13.15103 | -54.92445 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9bbe2c36-04a0-32bf-8bf5-2f859897fe8d | -9.71769 | -51.97103 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e2c0b218-55ec-3a85-a6f2-03cc6cc6bd1d | -9.04275 | -50.18274 | 2025-08-19 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4b09d70a-c157-38b5-8fd7-4b68bbf846c3 | -10.50759 | -54.6355 | 2025-08-19 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8fe52dac-74ba-395f-a44c-e7b909a15863 | -3.98866 | -42.53169 | 2025-08-19 00:50:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 393.6 |
| f68e2d0f-2cb7-3aab-8700-d42549ba4093 | -11.85713 | -51.58931 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14ecbb21-01d8-3cc8-bcad-6f25db6fd89a | -7.58425 | -45.44106 | 2025-08-19 00:50:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 11a3a114-2f68-3a5b-9cae-64230e594a60 | -5.74987 | -46.67736 | 2025-08-19 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 84745800-e002-38cb-b1ae-b9624754b49e | -4.9183 | -43.25533 | 2025-08-19 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 1c9076be-c266-31fd-8230-6f219125f84f | -11.74471 | -58.31501 | 2025-08-19 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9324a1fe-6eb7-3b82-94cc-3fe3ea95d835 | -11.85464 | -51.57128 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2317a7eb-3d75-3bee-a73f-70a1b8a34bd1 | -5.78257 | -43.63147 | 2025-08-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c9cfcb45-6065-3350-8040-dd5474d27513 | -7.26089 | -50.15192 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 289ac1e9-b631-3343-8857-37b5d3ef9f79 | -11.45234 | -47.32529 | 2025-08-19 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e6972e8a-9546-305e-834a-b73120b0269e | -5.77203 | -51.68517 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 82d4ff9e-edc4-3272-8cb4-6615f0e1c3db | -5.83739 | -51.6879 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17ef068c-8bef-31e6-9515-cec3c749a6c6 | -6.41992 | -53.37369 | 2025-08-19 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff165657-b4ea-388c-ac5b-0c19ddff157a | -5.78784 | -43.59282 | 2025-08-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 16cddd79-817d-33a9-90d6-b716da39da37 | -8.23634 | -47.85352 | 2025-08-19 00:50:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7e8a879f-7159-33ee-a0ab-e2544894796a | -10.96329 | -49.57096 | 2025-08-19 00:50:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c77c9b0e-47ea-3642-af27-c8def57fa4d7 | -10.03838 | -59.34318 | 2025-08-19 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f6da4778-6a4d-36cd-a0f9-4366f6a86efd | -7.26229 | -50.16185 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 08e36d75-362d-3843-b503-c58a71eb0df2 | -3.98342 | -47.88572 | 2025-08-19 00:50:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1c6e538d-480d-399d-aadc-0f2ace2159be | -9.51706 | -60.54949 | 2025-08-19 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ef98f12d-7772-3b9c-a8aa-15d8698164a4 | -11.85588 | -51.58029 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| f28008f0-e459-3235-a185-3273e36c868f | -6.93799 | -43.61327 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 618bc1ad-d381-3092-a7dd-e90436a5fde7 | -11.86474 | -51.57901 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 5f0aef6a-afe0-393f-b255-fafb1b991027 | -13.01655 | -56.83518 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| faf300e1-f348-3498-9b38-539a23b3d1c2 | -5.88172 | -48.12489 | 2025-08-19 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d9acf268-d974-305e-bad9-10d0faa6b0b8 | -9.70884 | -51.97227 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 29f86ffe-7e3d-35b6-aae6-4e026e60147f | -11.74726 | -58.33751 | 2025-08-19 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b77a2929-408d-3fb4-8410-34c81d3a0fc9 | -5.77759 | -43.59975 | 2025-08-19 00:50:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| f5824339-544b-3789-a770-b1fbaa236dfa | -3.98147 | -42.49621 | 2025-08-19 00:50:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| 9fd9a04f-2689-3d80-99ae-f8813d05ff3f | -6.63036 | -55.27163 | 2025-08-19 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 16b63ede-462b-3e9e-aedb-076540b09018 | -6.61518 | -43.87732 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7a2133cb-296c-36fd-b4a0-169258dfcabd | -6.94275 | -43.64269 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d64f8dea-dcc2-37c7-8fc7-b47e0a700fba | -5.57882 | -44.08349 | 2025-08-19 00:50:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| fa4043af-9b36-39e9-8a4f-8b922b6565b1 | -13.18578 | -54.94642 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4fc124ad-dafa-3dc9-ab0b-d61d1a38fd5e | -8.40024 | -49.50211 | 2025-08-19 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7361664e-baff-3a96-848c-6e1d864994d3 | -5.8667 | -48.11921 | 2025-08-19 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5956d8d1-3f47-374e-b5ac-04c8d99b8bf3 | -7.27081 | -50.17437 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e197544c-cfe4-3f25-b1a7-272204d8854c | -11.4472 | -47.33257 | 2025-08-19 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0b53a439-f19f-3cd9-a7f6-edb1f319981d | -10.04509 | -59.36295 | 2025-08-19 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| eb37540c-7c9a-3dd2-93f1-c3852ad96f56 | -13.16313 | -54.9361 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 9899f79e-f503-33ca-a985-67f070c78c71 | -13.17525 | -54.94783 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1000698e-5675-3443-864e-592ea9e1b1a7 | -10.04149 | -59.36856 | 2025-08-19 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ce3fa82f-2734-310d-8c38-8f6a7b2ca669 | -13.16472 | -54.94922 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8296b081-cd69-3eec-9a16-f102ebdfd034 | -5.87966 | -48.11116 | 2025-08-19 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 294d5aa2-b3ce-37ae-8c96-4d0174c51c0d | -2.54513 | -47.71439 | 2025-08-19 00:50:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a92286b1-7270-3fe4-9d90-0c19549ef5ed | -7.31093 | -46.30528 | 2025-08-19 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| dcd3471b-e4bc-393e-80f5-f72ba79ad761 | -4.02062 | -48.06593 | 2025-08-19 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a6b0026f-a9b5-3431-89a3-b56371f8e0ef | -8.77015 | -50.0143 | 2025-08-19 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 221e7e5f-acf0-3110-ba1d-d42f006c687f | -4.14655 | -46.46407 | 2025-08-19 00:50:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 210b4f84-c9f2-3178-9a1e-a54732245afc | -9.17834 | -59.6359 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a7c70798-9327-34ad-9410-c17787217569 | -6.618 | -43.90097 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 27e89bad-8319-3c39-8530-55c20882c577 | -9.57145 | -47.40127 | 2025-08-19 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c4c332ff-3c58-3d6b-bbea-65d4d1b16fee | -9.1842 | -59.65578 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2a28234a-852b-3939-84fc-2842878649fb | -12.30048 | -50.01794 | 2025-08-19 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 068d512b-8164-34dc-a8a4-7a2d1cc21968 | -13.15796 | -54.94248 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4384023f-706e-3297-98a2-6feb02bfac7a | -8.23833 | -47.86662 | 2025-08-19 00:50:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c8cc63c3-fb3f-371a-8a4d-8a132ffe1a9e | -13.14945 | -54.91134 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 242de130-17d7-3b7b-acc4-597b7cc302a0 | -3.38132 | -52.72152 | 2025-08-19 00:50:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 60883fde-258e-36c0-be12-9e33f43d413c | -6.93315 | -43.58344 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e15233a7-6892-3f9a-a676-7ab3abd6425c | -7.30825 | -46.28765 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b9978c2c-d03b-38cc-bf80-86c3cf5857d3 | -12.43137 | -48.70274 | 2025-08-19 00:50:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 05ff5386-23b5-3040-b2c7-52ec05f8bf94 | -13.35469 | -54.41314 | 2025-08-19 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 74e159cf-2836-3b2e-8497-2cca9c5bae4e | -9.04136 | -50.17316 | 2025-08-19 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c39e77ee-307d-31ef-91c2-a4148b3c05b1 | -9.71892 | -51.97995 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d274ad41-7000-3eb3-a750-29c11a815b22 | -9.07548 | -60.41105 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2e63444b-44ec-35a1-bd65-a6be4bcc8f6d | -7.97194 | -55.30378 | 2025-08-19 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a80fc869-58cf-35f1-a391-2681f416884a | -13.15461 | -54.91631 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| a79175ca-4f17-3ce2-8a12-020b691e02a1 | -5.54083 | -49.06959 | 2025-08-19 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 384b62eb-dfc8-3a61-bfbe-792921fb6174 | -6.49659 | -53.3936 | 2025-08-19 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 01df26a3-1cdb-3c47-b52e-894f954dda0c | -7.12185 | -50.41856 | 2025-08-19 00:50:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27157965-bb1c-3b25-a62f-34c8ca3ac34a | -11.68489 | -50.54805 | 2025-08-19 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7008d2c-3ac4-3db5-a8c4-11937e0a6440 | -3.98211 | -42.49081 | 2025-08-19 00:50:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |


[Clique aqui para ver as próximas entradas](README9.md)
