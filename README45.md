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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55c82d73-4b95-3010-8af6-24adeb704629 | -11.23372 | -44.95977 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b78ca6-c4b4-3b09-aaa6-1ed7048b1749 | -8.1949 | -49.60173 | 2025-09-04 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 364c55f9-70fe-36fd-a8a9-be854721db5c | -15.05244 | -48.36597 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35914429-f77a-35e7-a62d-d8f5fdb2da06 | -11.63354 | -52.20609 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6526d48-26eb-3c13-b3d9-ea8d56b459ee | -8.45241 | -45.04304 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccec8a7c-3807-3920-8240-136a746e860d | -9.60425 | -47.0347 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 44c6bc83-c34e-3b08-9695-6805f2546783 | -11.6027 | -47.78585 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92bf7dab-c81a-36bc-8b35-26bab97ea11d | -8.37329 | -52.54387 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7be3ad76-c1cb-34f7-a5a6-51d79651d70b | -9.61308 | -47.04322 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac0c526e-09a2-3826-943d-62ca4a71e5ef | -15.00858 | -50.02954 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 996b6869-42f0-311e-9c5e-e7500c92189a | -11.54732 | -47.31393 | 2025-09-04 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b58384-87f6-3188-bf3f-4302cef26b73 | -9.61525 | -47.02931 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbb2377b-e592-3672-b33b-268ddeed43ed | -15.18914 | -48.01242 | 2025-09-04 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85213075-4538-32c2-a910-64392efd8915 | -13.85854 | -47.97688 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2d0f795-d5c0-3436-98c2-36e217f358c9 | -11.13353 | -44.6369 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3291f5b3-70d6-3390-93bd-e58884a027ba | -12.88841 | -56.94363 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ff21288-88d4-3cd3-b396-e492401dca9d | -7.71485 | -50.24338 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9850c5fa-0c62-3317-8c19-533bb2f88560 | -10.75342 | -48.27151 | 2025-09-04 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 751dad56-b8df-33a6-9457-eaace6cd203d | -13.30768 | -51.76981 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dada9e27-ec94-380e-b9fb-9bce77cb163f | -12.88902 | -56.9404 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d13541f-7b59-3af3-8b35-9fb93e8c4c81 | -12.872 | -48.02159 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5840f5e0-d1ec-3da5-b2ad-b42033ce0bd9 | -12.87475 | -48.02565 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b87196-d204-3e7e-a331-75335fab2976 | -8.91055 | -45.87301 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 777c054c-28e2-3bf3-aef2-652b8de7c765 | -12.91495 | -57.00629 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb466e47-defe-3b6f-9c4c-ad58bf53a57b | -11.86963 | -51.46968 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d75979f-d997-3a9a-a6cc-98b2223d8b82 | -14.55411 | -48.07259 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff18bae-440d-3e49-ba45-005279ddc9e1 | -11.23663 | -44.96424 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ada259ce-2973-38ac-a2e7-d792cc8478f1 | -14.21698 | -48.07549 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6be9eb8e-a16b-3e90-b528-dfb109053553 | -11.61812 | -47.77397 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d788f200-60d1-3505-889d-9c69559c15e5 | -12.91334 | -56.93222 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6084f3fd-f734-3947-a858-2fe880df2895 | -9.43433 | -46.79355 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbff80e1-e2dc-3a6e-9ee3-515331ad3374 | -6.83154 | -59.36611 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7ea04dcb-3dcd-3a4d-bfd1-c7f5da8c8e2e | -11.12938 | -44.64046 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb502905-5947-3a7a-8e75-3ea39e458445 | -11.04789 | -45.14376 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 630a7396-0652-3606-90ff-e701f2ca36ba | -11.55008 | -47.31797 | 2025-09-04 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82389274-cf8a-3986-8366-b8091b15af11 | -14.82318 | -48.35339 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f0978de-4c9d-357a-ac18-36c859bbf9fc | -11.05485 | -45.40377 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead7c3c0-3ec3-3a91-b746-01ec859fb7ae | -12.95332 | -48.06779 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84c100fb-42b0-30b8-ae96-32f765679c5d | -8.89937 | -45.85673 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcf65e86-edd3-35ff-abbc-f2772433e4bd | -8.00856 | -50.10023 | 2025-09-04 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beb7c9c9-1364-3ff9-8e52-292948aa6f4b | -13.58272 | -46.91674 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff5bb4c4-d45d-3cf9-939a-4afc1ed644c2 | -13.44367 | -46.93622 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25955e13-8baf-354a-94d9-bd55bd37f2e2 | -12.4683 | -48.07841 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8e8af88e-f131-3a92-8b5e-62d9900778cc | -8.47629 | -45.0694 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d4b99c2-3986-3263-8606-bc989c26ad9d | -6.75193 | -58.73918 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a6fc08c3-76eb-3541-9df7-bf976ea7b8c6 | -13.56921 | -48.12868 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b42f6acb-08ee-338f-96b0-7fe56a453298 | -11.97454 | -45.7887 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb428d5e-47a5-3d8c-97d4-4a0d497816ff | -8.52592 | -51.32076 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fcdd488a-4502-3dbb-9d89-682ebff5a017 | -10.98325 | -46.8497 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa9059ec-59b9-336a-a846-33ef29006a3a | -9.262 | -48.55759 | 2025-09-04 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 911f617e-89e2-383c-813a-74ff4513c48c | -12.88779 | -56.94687 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28c497a7-0ba8-3212-b3b8-6cafce976f59 | -8.36915 | -52.54293 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ee3f33a-afec-3d92-b2c1-db5ea08b48e4 | -13.30465 | -51.78775 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3b017fa-c027-3827-b149-f247d8a42d9a | -12.86265 | -48.01646 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49c06255-74a7-38ff-8975-cc1346d9d253 | -12.96803 | -54.7645 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5bc9639-bef3-3fd2-8968-c36d342e3c3c | -8.34789 | -48.32901 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea6228ab-1402-3abb-b34c-067721fc1586 | -6.74007 | -58.73118 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 77cab5e0-27c1-3712-bef2-4d1c43ee4b27 | -9.48331 | -47.61126 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dee95eaa-0d65-3084-86ca-0d27693e3418 | -11.6038 | -47.77885 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8313140b-7081-35d2-a35d-a479bd8c8f22 | -15.03905 | -50.04259 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83e9b762-99f2-35dc-834d-b892650b7012 | -14.52109 | -53.1401 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bad7a80-0b25-3390-ba8e-ef98737045a9 | -11.85837 | -52.42151 | 2025-09-04 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b24a9f2d-d244-3924-a00c-e0496a54e04f | -12.24534 | -50.14268 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea69d9c8-10c0-3296-a711-d57ed373ae3e | -11.03805 | -45.13833 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| f727f5ad-03ed-3293-9785-ef1800daf5ed | -7.97204 | -46.33421 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a8bcb0b-75c0-3203-b1e0-32227cf8dcd4 | -14.93364 | -49.05505 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524ad839-c3de-351d-9542-65bca9ef890e | -13.00505 | -48.08347 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b046fee-6bab-310a-99cb-4bc83bd02623 | -12.48812 | -48.08167 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2439a64-3590-3ec8-ab1b-4891c936dd36 | -15.05575 | -48.36651 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08dedcec-9e8c-33b0-92d3-46b04506d6fc | -13.75236 | -46.94365 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfb52c2-b063-3490-8dd4-25b02b34df88 | -10.9915 | -46.84021 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e905981b-b2e5-3ea1-bb3d-c70ddcea431a | -7.85488 | -46.73817 | 2025-09-04 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5cbe6cc-4217-382f-af4e-43bffe0be080 | -12.91221 | -56.93139 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d4a321a-2840-349f-a684-27d28d8eaf43 | -9.49477 | -57.81562 | 2025-09-04 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ff17b9-9775-3887-b223-8a212e0e0a34 | -7.38953 | -49.39804 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bb71b9f-44d2-3cb5-a8e1-683cbe7db067 | -10.21758 | -51.13491 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e25025d7-dae8-3903-9ac0-29daa033af64 | -15.00525 | -50.0715 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15f1763f-32db-3f61-8275-6ac856f41e87 | -12.50459 | -48.06614 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27ebb849-c9a7-3403-9563-d2c9fdd32247 | -14.28351 | -45.22367 | 2025-09-04 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce56b45d-489b-3cb6-b6c8-c559e24259b4 | -11.8811 | -51.53697 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c28dec33-5b62-305f-bf1a-d324945bb062 | -13.50432 | -46.91973 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2602f2aa-ff98-3618-ba1d-0f68bfe2428a | -14.55796 | -48.0478 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec4b4e8b-24ad-3b96-868b-4256f6979451 | -12.48152 | -48.08058 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e956ae7-c54c-36bf-8b3b-d1dc9610105d | -14.81604 | -48.334 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47d673e9-7de1-37b7-a271-88236b69a6bb | -7.72829 | -48.72691 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eee55c2-8f78-3a63-beb5-6faa2e591e19 | -7.71416 | -50.24756 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab082ae3-9e3a-341c-9d94-231fd4242606 | -12.49016 | -53.83941 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c2bd305-dafd-375a-91ea-9a6f3bc3ad60 | -9.43483 | -48.08989 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5a1f5bfa-9871-3b24-b8f7-79fce5c3e237 | -11.03111 | -45.13729 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ea4d734-cdc8-3d4c-ab50-46aef43f3c33 | -8.07789 | -45.33836 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 641ad50f-3765-387a-9c88-eed008940f33 | -8.89603 | -45.8562 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 197edb18-16c7-3b55-ba41-903e20634436 | -11.7923 | -50.64035 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb651ee0-fde4-3bba-963c-31913964f069 | -12.2447 | -50.14658 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53a27c4c-c79f-3b6b-b76f-c16f710db86e | -12.9725 | -54.76541 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c4a0159-dcb5-3ce7-b813-8144e03e0604 | -10.11247 | -54.79736 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3674ada0-3e5a-3c99-aa39-b0e44120696d | -12.48238 | -53.83381 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efdd900a-e83c-3bf2-8620-96bd970f2bbf | -15.01474 | -50.03441 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 252da18a-09ab-3c36-b1b2-212499666670 | -12.87805 | -48.02619 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef64cee9-644b-3f0c-9362-5ca75fc858f1 | -8.84966 | -49.57043 | 2025-09-04 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1367b17d-1227-305b-8fe7-a736f41f2cb4 | -11.58469 | -52.15847 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README46.md)
