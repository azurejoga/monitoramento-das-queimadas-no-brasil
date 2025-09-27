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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8940876-4545-3fbf-9fe2-dd153929e62c | -22.58984 | -48.5816 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 66ff3add-1f98-3eae-9618-b7b3fd75debe | -22.3835 | -49.4819 | 2025-09-27 04:49:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf219b3c-4789-3cc1-99ad-046abe1a7c25 | -18.31786 | -57.12159 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3b6e0328-86ca-3738-81cd-c0e5d30513e6 | -20.1307 | -56.85292 | 2025-09-27 04:49:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d98a70fb-b80f-3d48-965e-c1ad6f2e57a7 | -23.02774 | -46.72514 | 2025-09-27 04:49:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 861ffc7d-3eb0-3f20-a98e-dab632e9a2d6 | -19.30747 | -48.90647 | 2025-09-27 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad0419d2-a5ad-30c0-b0f0-bf5296537262 | -22.59809 | -48.57688 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ff2c6890-c456-39a7-b4f0-858ef09e4ade | -22.37949 | -49.48136 | 2025-09-27 04:49:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d66f9c61-bc98-36d3-ba1f-2db6c3202852 | -19.40699 | -44.30815 | 2025-09-27 04:49:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da30cc7a-e37f-3a35-a50a-2b33023221dd | -22.27069 | -46.42712 | 2025-09-27 04:49:00 | NOAA-20 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 313e2f31-73ca-3727-a2f1-878be742b620 | -21.25059 | -48.58271 | 2025-09-27 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14583b74-a170-3ac1-a5b8-e493fb359d71 | -22.90472 | -51.19193 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b80b2367-b362-3828-9b0c-e7ac38d10130 | -16.7589 | -53.36187 | 2025-09-27 04:49:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7b11aaab-992c-3bfe-ba9d-a4b38016c9a6 | -22.59761 | -48.58104 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a9d551dd-ee14-3316-a872-92539fd8da2e | -19.05542 | -48.13287 | 2025-09-27 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ed1727a-24d2-3ee2-9fbe-61406235bd42 | -22.5839 | -48.58763 | 2025-09-27 04:49:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| a5377701-72ea-339a-b429-11ebf2eeaadf | -17.02721 | -52.23911 | 2025-09-27 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eac2b06-c4a2-3ab9-8e18-84b7df77ff1e | -15.89642 | -59.32809 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ddfa6f-05f5-3eab-81c3-a9f177a9fa78 | -20.13279 | -56.86176 | 2025-09-27 04:49:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13f6efbf-77d9-3cf2-b75c-638b1194b1be | -22.5883 | -48.59426 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ea68775-727e-39e9-8c24-6771afb0af79 | -20.73198 | -57.77481 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2249abf2-3fb7-3f49-820d-ac7b9652bd47 | -22.12933 | -42.33057 | 2025-09-27 04:49:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2cbd00e2-6545-3516-a393-9457e0da1867 | -22.59336 | -48.58043 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 3758c8b4-7b97-3742-8e77-aeeacc2b2470 | -21.18948 | -45.58842 | 2025-09-27 04:49:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5bb3a5e2-7bf2-3b98-a8a5-1f950f8fb04e | -20.65919 | -48.7855 | 2025-09-27 04:49:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6797ab21-1f97-38d4-92d6-6d6eb210c1fa | -20.43167 | -43.37125 | 2025-09-27 04:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8774bc32-bef3-396a-b4ab-6b8b99016873 | -20.4766 | -55.68113 | 2025-09-27 04:49:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1339a74-e515-36a3-9394-a181470595f7 | -22.8583 | -51.78509 | 2025-09-27 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0f89a035-65b8-31e6-b508-24bd468255b1 | -22.58341 | -48.59185 | 2025-09-27 04:49:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4fea3055-6790-313e-b1d4-1dc8d95a13e1 | -20.47751 | -54.54115 | 2025-09-27 04:49:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28fcb2cb-f246-3b8d-bd4c-7273d7b59322 | -22.36765 | -53.73415 | 2025-09-27 04:49:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a2a84e3b-ed79-31a6-8f05-78a95c15db4e | -18.29281 | -57.09143 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b7d9e14b-ec53-3342-9d6e-2c162a3d426d | -20.88593 | -56.60726 | 2025-09-27 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8d8b40bc-9323-3957-83e4-79bf86fc7f8f | -22.60433 | -49.02662 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a42ee362-f4a9-3fd8-b5c0-9fad13beede8 | -21.36162 | -48.09956 | 2025-09-27 04:49:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d119dc08-1cb3-3b65-9198-c92649045049 | -15.90071 | -59.32885 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98bc598b-35a4-3221-bbf9-285de5268607 | -21.85752 | -57.1162 | 2025-09-27 04:49:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c92dd14-53cb-35c7-99df-d3e2afe76d59 | -20.88662 | -56.60325 | 2025-09-27 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 17190faf-4910-3cdc-81b2-7c2441ecbfd1 | -22.71819 | -51.39082 | 2025-09-27 04:49:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9ef9d037-5132-31dd-b234-ee0478c00743 | -19.69834 | -45.89519 | 2025-09-27 04:49:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb8a47c6-bd2e-30a0-8407-d9215d9d0420 | -20.26296 | -47.95443 | 2025-09-27 04:49:00 | NOAA-20 | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 6377958a-174c-39d4-a41c-47325bc55e5c | -15.83417 | -59.61495 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcab5100-a7b6-3bec-8f01-4c3379c16470 | -21.35887 | -48.10164 | 2025-09-27 04:49:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbb1bfcb-a5f5-3420-834e-87f428d20859 | -20.99258 | -50.01035 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7b83c45-fffd-3ead-9d40-63297be46ae6 | -18.17852 | -53.33709 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5a2f87f-ff5b-3918-9f8e-1f95ef85d89c | -23.02832 | -46.71946 | 2025-09-27 04:49:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f8f323b2-cdb1-3168-b0f6-fd5533524da4 | -22.26132 | -49.56834 | 2025-09-27 04:49:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2eaf767e-8aa0-395a-9aff-5da47187b179 | -20.35737 | -48.78845 | 2025-09-27 04:49:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ced06f75-9e1a-3bbc-a197-65d028ae4294 | -20.1272 | -56.85225 | 2025-09-27 04:49:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ebbb322-e48f-34f4-b285-98f3be41aac6 | -21.19452 | -45.58928 | 2025-09-27 04:49:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7bcc5528-1c5e-35ff-937a-dc6ae613d56c | -18.31424 | -57.12089 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3e56e6c4-bb65-3f90-aec5-5714b8b58285 | -20.35329 | -48.78793 | 2025-09-27 04:49:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0186e218-b7d2-3948-aec5-3b4a11ad3ee6 | -20.79011 | -49.39342 | 2025-09-27 04:49:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c729f4bd-28e4-3f24-b139-39bd7de05a6a | -22.21355 | -56.19669 | 2025-09-27 04:49:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aa3dd7b-b50d-301b-908a-e0c825637059 | -22.72182 | -51.39141 | 2025-09-27 04:49:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3c89254f-bb55-39c8-a440-aba87889262c | -20.73763 | -57.78522 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ebff917d-3b1e-3838-83fb-04c78f94fb0a | -19.92747 | -43.6195 | 2025-09-27 04:49:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1c46fe08-6523-3ce9-8ed9-039c9ef45e83 | -17.73012 | -46.70999 | 2025-09-27 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dcf93b0-f9e1-332f-802c-7931992a7dd4 | -22.5946 | -48.57806 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| e8b5bedf-ad31-3723-b8d6-ac37e0691866 | -18.18127 | -53.34127 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e2a00fe-a408-3485-8b5a-c608fa57f491 | -21.11236 | -42.92197 | 2025-09-27 04:49:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f6dc79e9-214c-315e-b9ed-0719b9f9f839 | -15.93089 | -59.48763 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52a84576-733c-3b0d-bb96-83adb991427f | -22.58863 | -48.58401 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 490922cb-17e1-360a-a1c5-c0d33d6fc27a | -20.30372 | -46.66631 | 2025-09-27 04:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78935d5f-9b46-3424-94f7-673ac576015f | -18.30084 | -57.09105 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c60a044f-3c48-3c56-926c-97a4d991f4be | -18.32148 | -57.12229 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ada9f06b-b6af-3421-8765-da8df2224598 | -22.58508 | -48.58521 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| e7810556-622b-39b6-b94b-816631861c8a | -20.42 | -50.77166 | 2025-09-27 04:49:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3a1ad5fb-c2e9-37e5-8600-5d624db7b985 | -15.87864 | -59.3285 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7da4006-5ae6-3c01-b0b8-a8e7b68ef1fc | -22.59511 | -48.57388 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e00d7901-6bf2-3cd1-b85d-004bb54dc8c8 | -20.32441 | -47.1344 | 2025-09-27 04:49:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beacb765-2b44-31ef-8acb-b0b0974bbc7c | -18.25215 | -47.00817 | 2025-09-27 04:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89a38e8b-6de0-3da8-a885-f456001deba3 | -18.29283 | -57.09403 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fa3ccc38-d131-34fd-83ba-d67e9d299989 | -22.22652 | -49.72836 | 2025-09-27 04:49:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a858582e-d4d2-324b-93fa-d68de5fe72ba | -18.23983 | -55.38738 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cf8814ce-2154-33c1-abb0-74f481845bc9 | -22.88058 | -51.23772 | 2025-09-27 04:49:00 | NOAA-20 | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 05ab7945-ca12-3ac9-92b1-385be6c0b904 | -22.49988 | -52.98567 | 2025-09-27 04:49:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3aafce82-5a55-3c39-bd7e-4a26bbbc2231 | -22.36431 | -53.73356 | 2025-09-27 04:49:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| 79434fc2-5cb6-3f80-939c-99ed8db85268 | -18.29722 | -57.09034 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e29f481c-d473-3055-af81-48d974d4e95c | -20.17175 | -46.20507 | 2025-09-27 04:49:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a5dcf22-cb58-3dd8-a9bc-5c008cb28f63 | -21.35938 | -48.09729 | 2025-09-27 04:49:00 | NOAA-20 | PRADÓPOLIS | SÃO PAULO | Brasil | 3540903 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 479b1da9-65e1-326e-a826-0e56c4562f7e | -22.50045 | -52.98174 | 2025-09-27 04:49:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d5096e44-0a9c-313c-a5b6-abc3a5d7c0db | -18.18408 | -53.32323 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41850110-1fde-311d-9374-464d9d233d1d | -15.89148 | -59.33083 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee460b6e-c4ae-3e15-ab23-4aac31aab5ce | -22.58932 | -48.58585 | 2025-09-27 04:49:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| cbb62883-1d37-36b7-ab36-5ab24ad07095 | -18.18459 | -53.34184 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7171a957-966c-31aa-8f4e-3ece90400fda | -18.31502 | -57.11649 | 2025-09-27 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3b308967-20ad-3b24-b6f9-f8fa330d25c3 | -22.6048 | -49.02279 | 2025-09-27 04:49:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5fb31666-44ab-3f12-a1e2-813415312ed4 | -18.18571 | -53.3346 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 035fa304-71ce-3dad-a7e3-052c18a9fc08 | -18.17795 | -53.34072 | 2025-09-27 04:49:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f24498-ba41-3064-ae3c-8a262a0987a2 | -22.85771 | -51.78942 | 2025-09-27 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 25ded873-4606-3021-9161-dc6c87e2a8dd | -22.58456 | -48.58946 | 2025-09-27 04:49:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| fe26b63b-fa63-3f5d-a853-67e1735c0aa4 | -20.43741 | -43.37237 | 2025-09-27 04:49:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93663a69-2454-3e31-bc69-83c5b69ba497 | -22.71881 | -51.3863 | 2025-09-27 04:49:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 07b7ecd1-06ae-3b7b-983e-160dccb042bf | -20.99956 | -50.01637 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3cc115f5-87b0-3b67-be78-fc9bee9d23fa | -15.82464 | -59.61757 | 2025-09-27 04:49:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c12b9f24-0036-353b-bf9e-52d2cdd289da | -19.31146 | -48.90704 | 2025-09-27 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f21ff1-77cd-34d4-83ad-9bf5af9e2395 | -19.41216 | -44.3109 | 2025-09-27 04:49:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a44e139-9fde-3b68-bfa9-e3c0c0506371 | -21.00087 | -50.00658 | 2025-09-27 04:49:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 288f1424-7dad-3cc4-859d-d768431cf09a | -22.21693 | -56.19733 | 2025-09-27 04:49:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
