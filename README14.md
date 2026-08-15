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
| 983f8a2c-516c-312b-8478-3d3c55c84f47 | -6.98883 | -45.90031 | 2026-08-15 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 169c1780-1a6b-3a08-be33-d5d192cc24db | -7.23029 | -47.52403 | 2026-08-15 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c806081-caf7-3075-a947-718fa5adfc27 | -6.92371 | -43.63757 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5ad1186c-78b5-3f2f-b038-3fec584f163e | -6.9249 | -43.63017 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8668ce86-5c99-3adb-bb50-75ac3216dee6 | -11.48446 | -44.56928 | 2026-08-15 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4bc585-0ed1-37a2-bc82-1856f5f2aa10 | -9.97903 | -53.94868 | 2026-08-15 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 27046d5b-5b17-39d9-8440-bd874c38afcc | -9.11345 | -46.40021 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b7fd50c0-c98c-38ca-9bfa-ec4f77d814f1 | -9.47932 | -51.62117 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 819c780c-bbfb-32ca-b007-39e4ce1345be | -12.2415 | -44.10317 | 2026-08-15 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2c5aa2f-d082-3488-8ccf-4fd095542bac | -6.93372 | -52.789 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a13f6aa-2903-3099-b4cb-35b6851cbf90 | -10.75827 | -42.09003 | 2026-08-15 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba6d2b3e-35d5-3e6f-8198-96e1f6a62d57 | -7.22621 | -47.52271 | 2026-08-15 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3f22e51-ee9f-391f-a56c-5d1b605065fb | -6.36412 | -51.74902 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 610e5b61-e779-322b-965b-49b1311260a2 | -11.97086 | -47.38589 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cad38f80-aeba-3304-b319-f45d78022ca9 | -8.52105 | -46.53267 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 805f19e5-765d-3d21-8f01-f4274c62df77 | -12.38355 | -46.41745 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24009a4a-90e0-3fa6-84c6-ce40091cb67e | -13.42713 | -48.34642 | 2026-08-15 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81ed2bdd-f2d1-3c13-a286-9bf3fd46ab12 | -6.98071 | -41.29785 | 2026-08-15 04:14:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b20dfd08-ce80-3af7-ac8d-5fe21d380f05 | -10.29113 | -46.64587 | 2026-08-15 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a38a8a13-5c53-3a6a-b169-80f7aa441849 | -13.37686 | -41.34445 | 2026-08-15 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 35d9e582-0b48-3f12-9538-591358047471 | -11.40273 | -41.78518 | 2026-08-15 04:14:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48990b00-c4d5-31cb-86f0-96613579652f | -8.16572 | -47.40382 | 2026-08-15 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67780acd-6b40-35b4-8f3e-709fe8b3cb2f | -11.50911 | -54.64162 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a761d780-111b-352d-bc48-eae2d80aba85 | -8.93742 | -47.60172 | 2026-08-15 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b0983e3-963e-3ef5-b096-3a8c418451af | -6.33908 | -47.37768 | 2026-08-15 04:14:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3700c16-72d1-3d86-bdb9-fbb2999db443 | -11.40887 | -46.34607 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8786eaf7-5781-357d-8a81-2a419fc876a4 | -7.81155 | -44.11168 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c2a9765-d335-3851-a0bc-52c4ebe5e32f | -11.58181 | -54.68874 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cc23e16-71be-3032-8ae2-26a0f0a97409 | -10.517 | -50.16019 | 2026-08-15 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91639525-aaa6-382f-bc30-cc957e51bfa6 | -12.09707 | -43.16303 | 2026-08-15 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c67cf2cb-6181-303b-a9f0-09478dd5d5cc | -6.78747 | -55.83991 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b29f793-9bf3-3bc0-975d-d98fa87fcf45 | -8.08412 | -44.35294 | 2026-08-15 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e19165f-218a-3102-82df-cbc8acf35466 | -8.6506 | -54.70888 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90592a3-2f93-3c13-8b28-41332b250515 | -10.71993 | -50.56211 | 2026-08-15 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b16265f-e5a5-300c-b9d4-efc898c9094f | -7.72954 | -46.24695 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b674d69-0c6b-30db-afa5-8c98e1f794f4 | -6.9203 | -43.63703 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2d96286f-4c83-3201-8b5d-f9e6b3ca6eb0 | -12.37994 | -46.41671 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f12382c-ccf6-3c5c-a3b1-ca843e630dc1 | -7.00576 | -41.44065 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 481cce7d-7b8f-3167-b078-be9143dcba40 | -11.58803 | -54.68982 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e968151-a0c9-3bce-a457-a8f3e3136a1c | -6.79082 | -55.8466 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8b07076-7e09-3b28-8251-de221c53af86 | -11.40085 | -46.32649 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 823e5540-2b06-3ea7-81b8-8988802ba722 | -8.79295 | -47.92999 | 2026-08-15 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13d0e3ad-9664-3dc6-9293-26d3de55074b | -13.38028 | -41.345 | 2026-08-15 04:14:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e74bed0-3f23-370a-93eb-ef16bc4fb7a2 | -8.61028 | -54.67767 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f68f6595-cc44-3caa-8a99-50b0f9667a91 | -6.86458 | -43.87254 | 2026-08-15 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37f89561-65c3-3d4b-810b-2356011e3a1e | -11.3324 | -46.22112 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6e77109-154b-38e1-b7f0-7855a7aa25e8 | -11.41037 | -46.3345 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 736eff2f-c1a1-3f3b-a1e4-3ba6ac1eff49 | -7.45288 | -55.30218 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40b934c6-b7cc-3447-867f-85fe36675ac4 | -6.88442 | -43.70716 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32bbc241-0381-3e0d-95a2-d06ef8c97368 | -9.16299 | -45.82861 | 2026-08-15 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a295b94c-00e4-3d35-9582-896d43df2cf2 | -6.98099 | -41.46875 | 2026-08-15 04:14:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce7be0d2-2f3b-3886-8c62-998f9bcbe54b | -13.65398 | -46.25024 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e2ddfb1-5dbc-330e-8979-5ee04218e153 | -11.41695 | -46.33999 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7f001a9f-4ea2-3ab3-90e3-f3c83f0f1295 | -6.78885 | -55.83274 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77c8eb9d-a760-3840-8102-48e236551894 | -10.40563 | -47.97872 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6e4f196b-1175-3d5e-ba48-54fd4ef9704f | -9.48603 | -51.6147 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4a3b138-14fd-388b-bf32-a9cfe87bbcd0 | -6.93602 | -44.54487 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67c88222-550c-37f9-82bf-a8ce43488154 | -7.6873 | -55.15726 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b215150-bd2e-31f4-8748-b0ab0f31477b | -6.88009 | -41.9562 | 2026-08-15 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 254ee4ee-101f-390b-8632-3194d55a0a6e | -12.37924 | -46.42077 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8295c2cd-7087-3a5b-b4b7-2bf8687f718f | -7.59826 | -42.73838 | 2026-08-15 04:14:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48007a50-5410-390e-84af-5e3bd1e5898b | -6.82744 | -45.35479 | 2026-08-15 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a543872-a269-37d0-9a64-e84435a01db2 | -10.21744 | -48.47848 | 2026-08-15 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d18c21f-7bca-3417-ad7a-a0dcfcd9e866 | -11.67963 | -46.75345 | 2026-08-15 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d503e8-31a2-369b-b054-8e02368c9af0 | -12.70477 | -48.45741 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12858aa3-82c8-3da3-8644-f360edb5cfd5 | -6.79216 | -55.83939 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db19adc2-90e1-3581-879a-0d019be718c8 | -7.46537 | -49.62987 | 2026-08-15 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713589b6-0e3f-3e27-bf00-0193073cf629 | -6.92712 | -43.63811 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d2db3eff-0809-3516-934b-1e9aeaf98763 | -8.02527 | -55.14148 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c34fc18b-2966-3285-a3f7-9bba540568e0 | -8.50996 | -43.93723 | 2026-08-15 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e6a8f7bb-7e78-3c00-8d39-13b5bbecfa9d | -9.11714 | -46.40281 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5cc20258-e57f-34f3-b4d1-e072f92a2594 | -8.51721 | -46.53199 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1683bb12-508f-3441-8143-8e950585c29a | -6.93172 | -43.63128 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e7903e7-a982-30a0-8f5c-4edbd12cf69e | -9.48692 | -51.6174 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb909ac-8510-3ec9-8d41-e4b04a5221df | -8.60379 | -54.67631 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c00ac30d-a0d3-31a4-b83e-512a53efeb33 | -11.39502 | -46.3164 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60f38159-912f-3142-bac0-20a7a03b7be6 | -8.10554 | -51.66069 | 2026-08-15 04:14:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fe8f8ab-b31f-399f-8fca-ab2bb53c2c15 | -11.08212 | -47.2179 | 2026-08-15 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90f1ed6b-f803-3d8e-ac58-38f5272f32d2 | -11.59094 | -54.66616 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 581da8ce-07c8-301e-aba1-2210050f3e7f | -8.49353 | -44.74951 | 2026-08-15 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3676d3c7-d79d-399f-b47a-66453a0c453a | -6.98959 | -45.89576 | 2026-08-15 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bf671d-8019-3c86-bef7-c5b0e4945bc0 | -8.60386 | -54.67133 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8613061d-d36c-3487-b9c5-640305f6bebe | -7.01624 | -41.43873 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e1df053-4dc2-353a-8847-b2bbe12f7453 | -12.14342 | -47.16938 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99657da1-3217-3cc5-a56f-44667ab5f820 | -8.49067 | -44.74498 | 2026-08-15 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11c661b7-d02d-3bc9-bfde-e0ac9509406a | -6.78366 | -55.84526 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7cc7282-8d74-314e-adc9-8c4d5feeba34 | -6.8834 | -41.95673 | 2026-08-15 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 679814e0-cef1-3229-b4f0-ee05671676b8 | -13.54029 | -46.25781 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaffbf21-00c4-387c-9a8c-62651caa7f03 | -7.25803 | -44.21481 | 2026-08-15 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5780ce1e-fec0-3294-9c00-3a19d0d09662 | -11.42894 | -43.91729 | 2026-08-15 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69cb96ee-9505-37a8-9dee-ada55336a26b | -6.9243 | -43.63387 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b4f61cb6-a0d7-3097-a391-e6f26b3a03dc | -6.87734 | -41.9522 | 2026-08-15 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f2ce8d2-dcf5-37c7-a457-db19efe90752 | -6.9843 | -41.46927 | 2026-08-15 04:14:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 52be9451-992d-3b57-86ad-0a1d78864784 | -10.72092 | -50.55672 | 2026-08-15 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f85ef01c-7dbc-3d47-9db0-2b88a343a855 | -9.47999 | -51.61764 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 245fbd00-75b1-36ef-a24c-e9cc1604d54f | -9.13775 | -46.39476 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b653c4dc-378d-3332-ab7e-a372ebd510e7 | -8.02645 | -55.13532 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fcf6a650-bd3f-37a5-8573-55167ea225e8 | -12.35404 | -51.2143 | 2026-08-15 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c049cf0b-8193-3166-b753-dd410464078c | -12.72683 | -48.42782 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7886619a-eefe-39b8-87bb-525d64def3b2 | -6.78608 | -55.84712 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
