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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90e6a42e-d080-3df5-b239-271946dc9722 | -14.0035 | -48.7593 | 2026-10-10 00:09:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a830713a-e172-3f3e-978e-3e5b35b16e7d | -7.0194 | -47.6819 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72cf2f82-9af0-3a5b-94eb-f936a5522dbe | -9.9032 | -44.8904 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec94ed74-b879-325f-8df6-1cdcb5f48804 | -16.812099 | -42.3069 | 2026-10-10 00:09:00 | METOP-C | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45948331-566b-3e47-a3f5-5a68b4abacfa | -12.0198 | -43.492401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec004cc-36f5-3c86-ba59-3df77fa5a688 | -12.3642 | -46.597801 | 2026-10-10 00:09:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7916209-471f-3bdc-95b1-cc167038d034 | -13.9201 | -43.046001 | 2026-10-10 00:09:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e9189e11-6013-3717-a092-a183cc8de7e2 | -11.8263 | -43.593601 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e48fcfb7-5e6a-38f3-b13c-d3290f70bb5f | -6.402 | -43.7365 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 126f6f5f-9d4b-3965-82e2-8c24a0dac823 | -7.4778 | -42.844898 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d8092f24-285e-30ab-95ff-ea1234a3c88d | -11.5943 | -43.753899 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 017de9af-2051-3023-a04c-b8cf2471fac2 | -7.5302 | -45.3181 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a29a7d9e-8c03-340e-bd55-882bd69ce61a | -4.3931 | -49.7906 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d2c7c5d-6a53-38df-916d-290f929063c6 | -7.5325 | -45.328602 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9eae0e6-e0ce-3ce3-bf45-709bf3c09d4d | -4.2661 | -48.5672 | 2026-10-10 00:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad776d1-5cae-3ba1-a0cf-2e1b59f4f8ff | -9.925 | -44.896999 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97aaf7f0-81b4-37d1-ba47-ff2fa94dea4b | -3.1966 | -50.541 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6cb548-0158-30a6-b602-4e05a7ea0f27 | -8.194 | -45.7388 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be5d3a1e-e6e7-386c-a5e7-9c2c62d1815f | -13.2609 | -44.0033 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42a48a80-ecf4-3fc1-b0bc-3b22c3fd25e2 | -6.9134 | -45.869701 | 2026-10-10 00:09:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddb4992b-d7fa-3833-884a-bb23c766e69c | -14.5215 | -48.0359 | 2026-10-10 00:09:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bce49c6f-41e7-35d0-bb77-b1c495a94797 | -7.0096 | -47.683899 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb5291f-5eac-30f2-a1bb-4a6812773f32 | -11.9472 | -43.488201 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75d85250-5e57-3370-a2ce-aaad27af3fe2 | -4.5843 | -40.669998 | 2026-10-10 00:09:00 | METOP-C | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c2a8a877-ca05-34d1-b04a-d2b04dd9cb4b | -13.9112 | -47.841801 | 2026-10-10 00:09:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 985aec3a-76a2-3877-b532-3163048b58e9 | -4.3244 | -41.245098 | 2026-10-10 00:09:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6dc93899-37d1-3d68-9b92-0368b01abf41 | -6.825 | -39.560501 | 2026-10-10 00:09:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3bd7ed5b-2c67-3468-a2c6-40c167f79c00 | -4.9022 | -43.3312 | 2026-10-10 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1914584-f884-3493-9879-0a384e1f75c1 | -4.915 | -45.772701 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ed1c95b-15bd-345d-83ea-fbbdf978ce3a | -7.0065 | -47.669102 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13af69b9-348c-3aeb-b351-599c40e8eaf7 | -6.1928 | -45.431801 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d941955d-e8b6-3bb5-962d-11ce5701b2ea | -7.051 | -40.9506 | 2026-10-10 00:09:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf28f576-9105-3055-8de0-06cda97c293e | -5.505 | -43.0382 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dffe08b-6709-3b68-a18f-918af2721de7 | -10.8844 | -44.796101 | 2026-10-10 00:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e64d7e3-24ec-3111-a840-6db100821a99 | -5.5165 | -43.043598 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 696efe5b-f5e2-3c0c-b076-add753dcbb55 | -12.9889 | -43.334999 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10bc46f8-0fbb-399e-ad7e-a15f98639a99 | -6.2048 | -45.439899 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4f10664-b41f-3993-ae71-4e131fecc322 | -13.7304 | -44.303299 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76c74a75-60e3-385e-8fef-99a172633610 | -16.236401 | -44.060001 | 2026-10-10 00:09:00 | METOP-C | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37a5fcea-7b1f-394f-8003-6e07acc7b023 | -11.467 | -43.395901 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12d8e450-1d72-3d56-8705-334a5f8ec165 | -12.7725 | -44.899899 | 2026-10-10 00:09:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0aceab27-bc78-3b80-aad7-116fdf830d79 | -11.2643 | -46.380402 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58241e75-9e45-375b-86cd-6efdf3769964 | -10.8914 | -44.828999 | 2026-10-10 00:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ccc3b98-dac7-31e9-ae57-5bba6f48335b | -11.6546 | -43.7006 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11695f5b-0b4b-3904-b009-2acb73760041 | -6.5566 | -51.0882 | 2026-10-10 00:09:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef5faf5-65d0-39ac-b6a5-b13dc7f7c4df | -6.3179 | -43.497799 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44ebb8f8-e34b-3a6b-86dd-1699a827e144 | -14.4566 | -43.966202 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b63fd7b0-6582-35a4-8ec4-9abf0e453710 | -5.6739 | -49.0429 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf2c6c6-1806-3da5-a293-b2c0d53224e9 | -4.1164 | -46.880299 | 2026-10-10 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33a997f8-96b1-34f2-9814-f1db32f7fff7 | -5.8786 | -43.418499 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c18bcc0-b4cc-3fe4-a0a8-a2bc3b7dfd66 | -11.9647 | -43.474499 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 949d23c6-fdd9-3c11-9bfe-fb4e939c3522 | -6.8071 | -41.2379 | 2026-10-10 00:09:00 | METOP-C | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eeaca5de-f001-38d6-89b9-80ae7f825103 | -6.9999 | -47.686001 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3af96fc-47dd-3311-9bf0-5ae7edcf4899 | -13.3608 | -43.894299 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed1a437-b537-3fa5-b997-2e0148ab95dd | -7.6938 | -42.154701 | 2026-10-10 00:09:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80c3f98b-3b6d-3b68-a376-f3df60c34b10 | -7.1651 | -52.608898 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905fa7ef-ddc2-336f-a03b-c339cfea4fe2 | -7.7696 | -42.309299 | 2026-10-10 00:09:00 | METOP-C | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b45a51e-adec-3a7a-9d75-ee611c07a445 | -11.9549 | -43.476601 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc2a437f-03cd-3108-ab2a-1b68e9a498b4 | -13.3684 | -43.881699 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f64d017c-5963-3af5-9fb5-c8f4b6082f24 | -4.5889 | -49.199902 | 2026-10-10 00:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76e0327-9ffe-36fd-b95f-26a5463dbfa2 | -12.0255 | -43.471401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e218087-a8d2-3868-a638-000a0da51254 | -9.2733 | -47.418598 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2f23311-7d80-328b-a8e6-4eb7ca849888 | -5.6777 | -49.060398 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c05638-1169-362c-8203-6b22aa3b5067 | -6.4888 | -44.3578 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82181adf-2477-3870-aa43-0f7bd48f1612 | -11.8283 | -43.6031 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e175f8db-ab5c-33fe-9e35-99fee680e453 | -16.0042 | -43.608398 | 2026-10-10 00:09:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2725dde5-a282-3101-a099-cfea344a2159 | -7.5613 | -45.649899 | 2026-10-10 00:09:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 984b50a2-e405-3269-8f83-f4205d03cb53 | -6.6933 | -40.467899 | 2026-10-10 00:09:00 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 288b3ce7-a41b-3251-87a5-9509ab98fb99 | -5.6874 | -49.0583 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823e151c-19c7-31a3-883c-348e0f59a6aa | -4.3986 | -49.769699 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2204fe66-20a4-3d34-933f-c7d3914f377a | -9.109 | -45.814499 | 2026-10-10 00:09:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7465db8-b9b1-30c5-83b4-9724625d47e4 | -13.8857 | -43.916302 | 2026-10-10 00:09:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| deabf47d-cd51-3685-80fa-fb6942a845e1 | -9.4535 | -44.6045 | 2026-10-10 00:09:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fabe0fc7-e43c-3da6-ab8c-8cc9ee349a54 | -7.0639 | -40.962101 | 2026-10-10 00:09:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c2a3106-d56e-370d-ba73-078e2f6a8523 | -9.8828 | -44.794601 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 846958b0-7bca-3158-9daf-e586f2480081 | -13.1532 | -43.289902 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0a70128e-0542-338e-b20d-9a77202691ff | -15.2778 | -43.391899 | 2026-10-10 00:09:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e5215619-2abb-30e5-9140-2f580cf9ddb9 | -9.913 | -44.888302 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54d8897f-6fe9-3ad0-a8e5-030a3c080baa | -2.289 | -48.5438 | 2026-10-10 00:09:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5958ac20-9c37-3bf3-b339-571e53e0223f | -15.3911 | -41.911301 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 292c3962-d1b2-3491-a630-5b83b782213c | -4.9858 | -45.7682 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5d31bd-e793-3ed2-9411-8e9b79055cca | -4.6024 | -49.215199 | 2026-10-10 00:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c675698-e943-3757-9bff-b57081434145 | -15.2432 | -41.889099 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dca06aa3-0d39-3722-8eb8-9ad9e9afb90f | -11.9374 | -43.490299 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 040fc73e-90aa-35e1-b726-09d830515e33 | -9.2669 | -47.387798 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8992c92-bd7e-3d0c-bb74-2067dfdc5ace | -14.4424 | -43.946301 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a991e787-be64-30ca-afa6-455b6c4aebf1 | -7.2369 | -44.167099 | 2026-10-10 00:09:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b03c403c-c56b-3eef-93b4-04950165b86b | -13.3586 | -43.883801 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e48e41f2-ab93-34eb-a832-0588c06ee199 | -11.079 | -44.121201 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd1e0b4b-267e-3581-9380-8e8a452891ff | -3.662 | -40.2043 | 2026-10-10 00:09:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 342800e6-f596-33f8-96f0-a1d230076a65 | -3.5639 | -51.509102 | 2026-10-10 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7a8dc0-ce9a-33aa-8a0b-53d4a5f3610f | -11.9823 | -43.460899 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c44c0e69-2516-3902-961c-609b99b2a7e1 | -11.465 | -43.3867 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 541cbc2d-63fe-3ca0-9097-97bd6ddc18a6 | -4.4182 | -47.547501 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31896b0a-f0cd-347d-a804-36ee907ed8f1 | -11.602 | -43.742199 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d56520a-99e6-3fa9-8696-00bbbcbaf07e | -3.6718 | -40.202099 | 2026-10-10 00:09:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 94feb675-e2eb-3cde-adf9-0f6bb0edafbd | -11.6049 | -43.611099 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0bca30b-6ac8-37ea-a44d-0baa3ec60f50 | -4.3889 | -49.771801 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e898e783-db9c-3f59-9462-b4a6ac92906e | -4.7817 | -42.7537 | 2026-10-10 00:09:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc39c1d3-fd1c-3fd7-a172-2208ce38e978 | -14.0529 | -43.836601 | 2026-10-10 00:09:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
