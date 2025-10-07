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
| 474e3200-5151-3a3b-9608-fc8b049a8a10 | -7.78273 | -49.84605 | 2025-10-07 00:13:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 72cadf02-10e6-3a05-a965-e61954307bcb | -4.44243 | -44.14307 | 2025-10-07 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ed36f1b-ec4d-3e2e-aea3-9e580a95fa4d | -6.32372 | -41.61664 | 2025-10-07 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1fb400cb-0a5f-3c50-8676-0ce5f96248f0 | -6.2499 | -43.88137 | 2025-10-07 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58fdaadf-781d-3ce0-965d-a7e411a49987 | -8.17995 | -50.30993 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 3c566821-70af-3602-97ca-a5c9d2b3f60f | -6.07704 | -44.83897 | 2025-10-07 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bca6cf5-4c2a-3d5e-a75e-dd452c34e8c7 | -8.38553 | -41.84599 | 2025-10-07 00:13:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a051f4c0-0363-38d8-9b00-6bab5db8b84f | -6.58228 | -44.62301 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c83da601-2ed6-33ce-8b70-452d56dfb41e | -6.49934 | -41.55608 | 2025-10-07 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7b85e7e9-7b10-3bde-a367-b27946eae9e3 | -8.1767 | -50.2975 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 07a6c9d9-aca1-3d3f-ae3d-27ede05cb712 | -6.72167 | -42.84727 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 09d47425-3810-3b9e-ac83-038b22952104 | -4.91867 | -48.02789 | 2025-10-07 00:13:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f16f9662-76c2-365f-8207-1f557f4a4a41 | -3.57015 | -43.51479 | 2025-10-07 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dd72aedb-d2e6-3a21-aa99-2a88f5442ba7 | -5.24659 | -46.5783 | 2025-10-07 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6b25682-97b3-3e4e-8330-9b68a9cd2dbd | -4.58368 | -48.12142 | 2025-10-07 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d2b45fd8-ba24-360b-be0d-be8e94046ad3 | -8.51329 | -46.30471 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1b4e54fe-559b-3f6c-8bfa-bf69edc11aea | -7.45772 | -43.03262 | 2025-10-07 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 41894571-fd57-361c-b0ce-1cb189f32a62 | -6.12909 | -44.48448 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 720c25fe-de10-37e3-b58c-3288ae053d6b | -4.80268 | -44.61424 | 2025-10-07 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bf943d24-4e66-3796-834e-2be2ef66755e | -5.60333 | -47.49913 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 5b84cac7-b49f-312c-a356-c669f204138e | -8.55625 | -50.08404 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f1f2a2e6-2bcd-38e7-b690-f5463fe2542b | -8.22607 | -49.87243 | 2025-10-07 00:13:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5cb78a7c-ab0b-3adf-b20c-20649e7e09db | -8.56816 | -48.24827 | 2025-10-07 00:13:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 17027de2-7c76-3c84-9e7b-87e871bc264a | -6.15859 | -42.58961 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 8b8b35b6-e9ec-3eec-9d8a-97b21c49b8a6 | -3.11171 | -40.99188 | 2025-10-07 00:13:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8503b23e-de9d-38a0-b075-b99d28f428e1 | -5.74871 | -44.98477 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9996a37e-041c-34ad-a23b-b4ca9ca9bbe6 | -6.98253 | -42.86778 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 3a78e8df-ffa2-3be2-b0ce-d8e28e8fef92 | -5.79384 | -42.48675 | 2025-10-07 00:13:00 | TERRA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 36a214d1-a1f4-32c0-aacd-9d0ddace4b56 | -5.25451 | -46.56738 | 2025-10-07 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 70601b3c-ff6d-3f14-863b-9c39814f87f2 | -4.51673 | -40.93609 | 2025-10-07 00:13:00 | TERRA_M-M | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3fc1802a-85cb-3760-9533-ccd10223b170 | -5.59714 | -43.11214 | 2025-10-07 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 15.2 |
| b12d2d4a-e9ac-37ea-b5c3-5817ee43f813 | -5.59771 | -44.42871 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| bcddef7b-4533-32a5-9e51-5f421f46bf38 | -5.6898 | -44.63981 | 2025-10-07 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c01e397-75a6-3b83-a0dc-709e6bc5226e | -4.69483 | -45.83866 | 2025-10-07 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56a527a9-6a2c-3a93-a464-ceedb614eb46 | -6.12788 | -44.47568 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ed0ab05-7a8f-33d5-a58f-008b3fa5b45d | -8.50324 | -46.34307 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d869f5a2-9cf8-3f08-81fb-f96322f65429 | -6.23778 | -43.27602 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3f65e5a0-3333-324e-be69-005f58aad85e | -6.59109 | -44.62177 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| db163e84-0c09-304c-b01a-6c898c1dab3b | -6.65144 | -41.97108 | 2025-10-07 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 080f67ea-bd66-3752-9d52-38b380a04c66 | -3.42738 | -43.15266 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8416f94d-2991-3837-84e2-7243efd6f3f4 | -6.92747 | -45.25475 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dabeb8dd-3d94-3d36-a2e6-92039baef7cf | -6.05225 | -43.52882 | 2025-10-07 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f28982dd-fa24-3b64-a143-c60c90dc76e2 | -7.61329 | -45.4886 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bd7ea75-575b-3bbe-a0d1-234aba7f8ad6 | -9.03808 | -50.60178 | 2025-10-07 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 1ab670b1-6f50-309d-afc5-c7edd5a32651 | -10.38197 | -50.29836 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9c616235-9769-30ee-bda9-25278ea242db | -7.72661 | -42.39391 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 378165ec-9b94-3395-b245-ececcd9daabd | -6.7126 | -42.84863 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d2379531-1e69-3deb-a88d-a3d04e6909ec | -9.59099 | -47.84336 | 2025-10-07 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 31a720ba-69cf-315a-b726-1b28297310cf | -5.66642 | -44.26031 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5413d7c4-8133-3029-9e61-4cd5be1f6ae7 | -8.60401 | -44.91263 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7d14240-9d9f-35a0-87f0-c31810435cf4 | -4.29165 | -42.02108 | 2025-10-07 00:13:00 | TERRA_M-M | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2f10bfb7-0524-3d98-9c5a-254f391f8188 | -8.64323 | -46.30116 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| cf19216d-f3a9-3e96-a4fd-2f1c912da5d0 | -6.5835 | -44.63182 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 78ffd60c-5e0b-39df-8521-2e2cc7bc9638 | -5.97672 | -43.51821 | 2025-10-07 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 34119975-efb8-3fec-bfd0-1c7212111e95 | -7.90804 | -46.85081 | 2025-10-07 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7ec72d04-c606-343a-8d1d-8aecdd8e6f2f | -7.86102 | -46.7921 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 74c9f5a1-9311-3d77-a1d4-743438790e06 | -5.21863 | -47.37787 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9e2f7543-8adf-3ee3-8a73-d7b0e2802fad | -7.62102 | -45.47799 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9920af24-deeb-3a35-a2c5-0c303ff54b65 | -4.6859 | -45.83986 | 2025-10-07 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 2fe65a61-15a3-30cb-ad43-1341e450369b | -6.44894 | -44.58534 | 2025-10-07 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fec51c81-ca11-32bd-be47-5e8ca8031faf | -6.5189 | -43.56947 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9ca56f8-05a2-3a47-a9dd-bc98747371a4 | -5.79799 | -45.21278 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fc615779-ee0b-3046-8412-b72bbc09f6f1 | -4.0924 | -40.13325 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 049e1797-8519-36a4-9066-f2e8e38f70ab | -4.64971 | -43.19128 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b8075437-78eb-3d6e-9aca-6889380cb656 | -7.69132 | -42.40883 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 6e31e57b-a399-30e5-b85a-cdfc0b2b5e5d | -9.23803 | -51.83849 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b3d414b9-fbe6-32fd-890e-428bd3e55a3d | -8.87342 | -47.97305 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b57ccf76-4a23-3c12-b6c6-545371d6c4d3 | -8.6499 | -46.27927 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 558c3439-5598-37d5-8547-ff0776d8449c | -6.2581 | -43.286 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c217ae86-100e-334b-8c6b-bcdc44967dd8 | -9.03549 | -50.5967 | 2025-10-07 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fefde3ee-126e-3bec-a71f-026a25bf8b5e | -8.60647 | -44.93077 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e1ef4250-c247-386e-96a5-4d5020c40b8a | -8.51462 | -46.31487 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 9fa09ce4-9ef8-3d76-a05a-8101201caea8 | -8.18358 | -43.34758 | 2025-10-07 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2170961e-40e6-367a-b0d3-a1683da223a4 | -5.7433 | -49.13204 | 2025-10-07 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 79749a28-a2df-30aa-b831-da6024737cea | -4.14144 | -47.65275 | 2025-10-07 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9f0edfa6-4acc-3d96-af53-daa52cc219bd | -8.17346 | -43.3399 | 2025-10-07 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8d34cdf4-00b4-3cb6-842d-c4f6d7c9b8b8 | -6.25681 | -43.27689 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 40e0b526-adf6-3704-b3da-c5b51537972a | -8.87451 | -47.68102 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 606e7eb7-621f-33e3-9a28-357a9986472f | -7.67982 | -42.58247 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a6bb075e-ca88-3670-bab6-604c481b662b | -8.88328 | -47.66724 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2cfe5911-55d9-3a6f-8ff6-9b82496540eb | -4.90602 | -43.44067 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5ff5382-6185-3f42-8bed-bca9f026903d | -5.61177 | -43.93377 | 2025-10-07 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6599a8d3-1387-3cd5-a0ac-26def58c7677 | -6.98386 | -42.87716 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7dcc6eef-f084-3fa3-b6ed-ead95dbb8e5b | -4.89783 | -45.57837 | 2025-10-07 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 948eb991-1817-3785-9e2e-3a354be5fe1c | -7.78512 | -42.60895 | 2025-10-07 00:13:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4d056664-99d0-36c7-89f2-8f5238678b47 | -10.87046 | -51.01457 | 2025-10-07 00:13:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 1f3d9b3a-75b3-3bab-98b2-8be5618e9ed1 | -9.98157 | -48.02677 | 2025-10-07 00:13:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 78888e64-8cd1-3812-860a-e2298839160e | -5.79604 | -45.47416 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28063ce6-4c53-37cf-80c9-84dd1e9f32ac | -5.46752 | -42.91544 | 2025-10-07 00:13:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0e5867aa-a831-3548-a02b-b4cc4c1b2b10 | -6.81564 | -39.41111 | 2025-10-07 00:13:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7353b195-d952-326a-80d6-80b609b0fa16 | -7.78645 | -42.61834 | 2025-10-07 00:13:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 37eeeb15-684e-3a4b-bfd3-8843abbcded3 | -5.75678 | -43.3948 | 2025-10-07 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ab8a801b-3b77-3e45-8b7d-9858e4c6cec4 | -4.21757 | -49.99845 | 2025-10-07 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 44676618-b25e-3a6e-abec-e4754415d443 | -10.3975 | -50.31768 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 01da38b5-fa46-39e1-9bca-8db6b41bcee1 | -7.23667 | -46.46171 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3a574753-c049-336b-b727-f024a1102fc2 | -5.54513 | -42.68141 | 2025-10-07 00:13:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a815c2ea-e3dc-3c3c-886b-5e48c9b8e9b0 | -6.69709 | -42.86992 | 2025-10-07 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 02eba471-5e0a-3cfe-b2f0-6303cb978826 | -7.2686 | -45.32143 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c720add-0b82-3646-8667-79153f843f74 | -7.58235 | -45.9405 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 98a50332-2346-3dc1-a16e-cdd5b5eb2f26 | -4.38068 | -42.98857 | 2025-10-07 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README9.md)
