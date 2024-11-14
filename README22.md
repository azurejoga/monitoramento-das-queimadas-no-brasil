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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3636c9ae-549d-37d4-933e-b3f06e186894 | -9.21027 | -36.57688 | 2024-11-14 03:49:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3ae926b8-b021-3586-8065-6c297964988a | -10.25653 | -36.46239 | 2024-11-14 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5c7d0f51-6328-3bba-8612-2c1e59b1ecd1 | -10.04445 | -38.14488 | 2024-11-14 03:49:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49b3ef6b-c3cd-3a98-84cb-1e21ecbbb88e | -9.48758 | -36.84629 | 2024-11-14 03:49:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2222403c-c64f-3992-835e-efe281fb8f00 | -9.7304 | -37.05341 | 2024-11-14 03:49:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8a6b3cbe-6bc1-3f15-b21a-0b61c8e4763b | -19.577 | -54.89762 | 2024-11-14 03:49:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e44fb76-9f31-36bb-9f6c-5043515f2410 | -9.03308 | -37.62389 | 2024-11-14 03:49:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 187b67fb-04f3-35b9-8ca9-b480b0d595ac | -17.5869 | -57.5533 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 9bde5f6f-9443-34ce-b64a-35dd63d360ca | -1.7921 | -52.186 | 2024-11-14 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c087c58d-7dfb-372e-a0a1-c5b73ae9ce25 | -1.8105 | -52.1857 | 2024-11-14 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| be01ff94-dd41-3de4-bf7f-baadefea1c69 | -4.5614 | -48.0141 | 2024-11-14 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d8e1c7e0-ec2d-3652-b03c-c49b1b226feb | -1.8106 | -52.1652 | 2024-11-14 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1d455a91-ea2c-3ecd-b167-cafe892ff497 | -17.5675 | -57.5351 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 50948802-8815-3393-ae1f-cca610b6f977 | -17.5879 | -57.4917 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| d3365bca-f00b-30f1-b711-2519f44a1f5b | -17.5872 | -57.5328 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 723bd9b0-445e-361c-bf6d-cc91ad8d85f2 | -17.6066 | -57.551 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 90187ae8-4128-38ed-9435-24f662083717 | -6.0472 | -44.0331 | 2024-11-14 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 596bbf47-cc5a-37ff-a78e-ca94499667c4 | -1.7922 | -52.1655 | 2024-11-14 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8c3e9dc7-c7dd-3f66-bef7-de42cfcc6312 | -1.3894 | -51.1197 | 2024-11-14 03:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| abbfddf1-e496-386b-9f29-d914aae52493 | -17.2543 | -57.4698 | 2024-11-14 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| ef4af992-b61e-301d-8aea-e14cba88f19d | -17.5672 | -57.5557 | 2024-11-14 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 9cfc73ad-3d66-3bf2-90a7-2bdae161ba71 | -2.2729 | -45.347 | 2024-11-14 03:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 14e3e3d7-24e8-32d2-a0bc-d9161f94aea2 | -23.59033 | -47.44081 | 2024-11-14 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 221f537d-8454-35c7-ad27-46bb5c270b2c | -23.10609 | -52.10011 | 2024-11-14 03:51:00 | NOAA-20 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 64bec192-f086-3533-8b21-0e42438ecfde | -23.10032 | -52.09886 | 2024-11-14 03:51:00 | NOAA-20 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 652fd685-4376-3274-849f-5e6ef984bd69 | -23.95879 | -54.05198 | 2024-11-14 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 462c9369-98bb-3651-b812-3769d0375aa0 | -20.89069 | -49.97094 | 2024-11-14 03:51:00 | NOAA-20 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9af3e7a2-fc44-3876-a24f-a860d4225105 | -28.58258 | -49.44376 | 2024-11-14 03:51:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ab4f266-c12d-39f3-bffe-ee9ec37a3f1e | -22.53652 | -48.81631 | 2024-11-14 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecb1db0a-fb5a-37f8-81dc-06b0761d9f1d | -23.96017 | -54.04647 | 2024-11-14 03:51:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9e8c9960-9d64-30b4-b594-6cc43e93f037 | -20.89594 | -49.97229 | 2024-11-14 03:51:00 | NOAA-20 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cbd6156b-b62a-3e66-897c-12c4754703a6 | -29.77852 | -51.18096 | 2024-11-14 03:53:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| a5e5694a-fa50-39c1-a505-9d7bb7624c36 | -29.87287 | -51.16079 | 2024-11-14 03:53:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 2c987403-06ad-3211-b9b7-3e6835fbfc3c | -29.77383 | -51.17955 | 2024-11-14 03:53:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 672c1a1b-ec50-3598-ae82-09330c60ca19 | -17.6066 | -57.551 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 93f2bb77-64f1-3eec-b8c3-963f14cf1db4 | -1.7922 | -52.1655 | 2024-11-14 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2428a14a-081a-352f-ba9a-662980245bdd | -2.2729 | -45.347 | 2024-11-14 04:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b9d5c920-5308-3dc1-b941-d40f0f5fadc0 | -17.6076 | -57.4893 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 79cf5c1c-9c6e-3ac6-940e-4e65db733073 | -6.0472 | -44.0331 | 2024-11-14 04:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f6e55ead-9dcd-3c3e-b399-dd97a90d3183 | -17.5872 | -57.5328 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 363ae8a8-3ab5-3ab8-8c0f-827ca9eefaeb | -17.2543 | -57.4698 | 2024-11-14 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 6d8c4479-9595-38f3-8b6e-1b2e51162ce8 | -17.5869 | -57.5533 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| faaaffae-f50a-3d57-9c19-52cd3da5c051 | -17.6079 | -57.4688 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 21ce8c5c-ec4c-3c2b-939b-6346ef8134cd | -1.8106 | -52.1652 | 2024-11-14 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| da33dfe5-11a3-3a99-a530-2996c2bfa675 | -1.8105 | -52.1857 | 2024-11-14 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 41759369-7eba-3608-9f8c-cd98b23a5ca1 | -17.5675 | -57.5351 | 2024-11-14 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 5810d04c-5b17-3116-afbe-0e76ffeb2127 | -17.5675 | -57.5351 | 2024-11-14 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 264734a1-b900-337b-ae95-7383fe3a4ffa | -4.5614 | -48.0141 | 2024-11-14 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9dba6796-0858-399a-82ad-1243d8483dc7 | -6.0472 | -44.0331 | 2024-11-14 04:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ccf19928-a53c-3dca-9bea-e25beec99ef5 | -2.2729 | -45.347 | 2024-11-14 04:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f077e59f-a5f0-302c-84da-623782632a67 | -1.8106 | -52.1652 | 2024-11-14 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0e21007e-9c63-3aea-8b02-6b7c42d444eb | -17.2543 | -57.4698 | 2024-11-14 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| f38bbd72-2b9f-336a-a0dc-25df379fd4e6 | -17.6066 | -57.551 | 2024-11-14 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| fdb7c84b-e928-30e4-920b-1e715430e59c | -17.5872 | -57.5328 | 2024-11-14 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 22a7388d-5c22-3abe-909d-20e8b016f115 | -1.3894 | -51.1197 | 2024-11-14 04:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3b3166c9-8932-3146-9707-345beb4d6c5a | -1.8105 | -52.1857 | 2024-11-14 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5b31d798-de0f-3d0b-8c89-ed8937f77a2a | -17.6079 | -57.4688 | 2024-11-14 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| e6e46f4a-ba11-3405-bc67-63abe80a75e3 | -4.5616 | -47.9925 | 2024-11-14 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 32d158c0-92e1-3864-bef0-505bc6a72b24 | -1.7922 | -52.1655 | 2024-11-14 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5ef2f909-00fb-39dc-b337-b80a748cc617 | -17.5869 | -57.5533 | 2024-11-14 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| b28992d4-766b-3288-9f1f-6c51465c7e39 | -1.3894 | -51.1197 | 2024-11-14 04:20:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9bb4fe75-c578-32fc-aea4-b7b2fce4ad14 | -17.5872 | -57.5328 | 2024-11-14 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 5761f96f-afe1-38f5-82bd-2fb01e3ee744 | -17.6066 | -57.551 | 2024-11-14 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| aa9eea57-f122-3a20-9062-9aba6ecf66a8 | -17.5869 | -57.5533 | 2024-11-14 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 8231a7c4-dc42-3775-99ee-cd2e3a647621 | -1.8106 | -52.1652 | 2024-11-14 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5a9011c6-b30c-385d-91de-0133b931ef26 | -1.7922 | -52.1655 | 2024-11-14 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1caf19ef-10aa-3a78-b1ac-40a801dd586c | -2.2729 | -45.347 | 2024-11-14 04:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 688629e8-5980-32a7-b18a-c47a455f74a7 | -4.5616 | -47.9925 | 2024-11-14 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fdc1be14-b08d-392c-bac5-826fecfbc216 | -17.2543 | -57.4698 | 2024-11-14 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 1a0b54bb-95ad-3bd9-b5ee-e7f482dec724 | -17.7052 | -57.5392 | 2024-11-14 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| e796e893-f946-3e90-94a6-8921467f9dc7 | -4.5614 | -48.0141 | 2024-11-14 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a9764688-2859-3a50-bfe8-e7abe4f8690c | -6.0472 | -44.0331 | 2024-11-14 04:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 115de2ad-fb41-362e-86f6-cc2f1ff98795 | -17.5675 | -57.5351 | 2024-11-14 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| b3db2bcd-0121-3e7e-a0d3-c6d5e1631a95 | -6.0472 | -44.0331 | 2024-11-14 04:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| fbc73456-bc09-336d-9c4d-6965e4e48024 | -17.2543 | -57.4698 | 2024-11-14 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 6efebd9a-f923-36c2-9e56-1c2c7b6e4121 | -17.5675 | -57.5351 | 2024-11-14 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 7a7dc779-efb8-39af-b137-a2068ca0cba6 | -4.5614 | -48.0141 | 2024-11-14 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 10ee483d-aea5-3a39-806f-0b9f1bc96e9a | -17.5872 | -57.5328 | 2024-11-14 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| aca22cc4-df24-35d7-9cc1-6523fe095681 | -17.5869 | -57.5533 | 2024-11-14 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| fc609589-d0b7-3b66-84bb-e15833650172 | -17.6066 | -57.551 | 2024-11-14 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 836a3efc-5abd-365f-807f-101d8b7c18e0 | -1.8105 | -52.1857 | 2024-11-14 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 880c4188-d501-3dbf-b4fc-cb808a94c2c2 | -1.8106 | -52.1652 | 2024-11-14 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 68a1be55-99df-3607-822e-82f6600c0944 | -2.2729 | -45.347 | 2024-11-14 04:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2e3b9551-e239-3063-ade7-a30eb52c645c | -0.29295 | -48.42587 | 2024-11-14 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa63a164-d4e9-3169-bbd0-901b797490f9 | -0.20536 | -51.52604 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b288e5bb-fe86-30df-aa71-d1ac91e23b73 | -0.29625 | -48.42638 | 2024-11-14 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6d401d8-b0a5-311c-aebc-ec0513dd8a4f | 0.68486 | -50.49409 | 2024-11-14 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bca2040-4405-32f2-8daa-a8665e8099c4 | 0.69545 | -51.44038 | 2024-11-14 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 560e4b01-adcf-3918-93ea-92fbae56cca1 | -0.0141 | -51.1448 | 2024-11-14 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bbb2be3-3184-3435-b92c-37cb1e7652d3 | -0.19346 | -51.50707 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6290bbf9-d343-3b0c-ab87-759300fcfa86 | 0.31231 | -50.77203 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10dafa09-16fd-3a34-9a72-775988a82293 | 0.84705 | -50.20887 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 810ac58d-c14c-34bb-87f7-450216c7b577 | 0.65532 | -51.78233 | 2024-11-14 04:38:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90cbe746-f252-34c1-921f-72277188c146 | 0.03389 | -49.40686 | 2024-11-14 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6a45270-4253-3e83-8407-788aadf21fa8 | 0.00182 | -51.13 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3775052-e3ea-3419-a5e5-19a6ce373c95 | -0.15659 | -51.45866 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e42555-c57d-3469-9e19-bc114f002a8d | 0.31582 | -50.7715 | 2024-11-14 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f8802a8-485e-3cc6-844a-5cb8a3353927 | -0.20303 | -51.51712 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14e16478-ce06-3d69-adf2-a5badb613e53 | -0.20201 | -51.49982 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b69c2164-3867-3038-852b-1919beb26bda | -0.3689 | -51.42169 | 2024-11-14 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
