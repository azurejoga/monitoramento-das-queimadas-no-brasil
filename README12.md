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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c36cd15-7c2d-3034-a101-c793279fafeb | -3.66835 | -45.22792 | 2024-12-13 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8784c4ae-92e6-322d-b70c-46a7da8c56db | -8.16402 | -43.81993 | 2024-12-13 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| efdb214a-4c51-3dde-b209-3cf9c5db14a1 | -4.26709 | -43.83077 | 2024-12-13 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b11cced-e03b-3a23-a502-94f1ea988a0f | -4.44758 | -44.65366 | 2024-12-13 03:55:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06038738-574b-3fc7-b019-8c42427590bd | -6.11369 | -43.95463 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82ee6845-4e3c-349f-83a9-797d955e0655 | -6.91185 | -43.52997 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e98a972e-80e5-367b-8b83-2c389f02ade5 | -8.26433 | -35.21342 | 2024-12-13 03:55:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16525df7-c4cc-330d-b405-5fb19cef9987 | -5.42041 | -44.86303 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c919f48-109c-3525-b18c-ebb9e411f2da | -3.07092 | -40.04989 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 253b33df-2a74-3e9e-ba70-f2dfbfd6c743 | -3.26936 | -46.91759 | 2024-12-13 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f751b2f5-836d-3000-9eee-32268063a64d | -4.16433 | -42.4403 | 2024-12-13 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6829fc5f-fa82-3911-909f-6fe5c83c89eb | -3.27426 | -45.49445 | 2024-12-13 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9113698-9bc6-3aae-bd4a-31231710ee3d | -4.97663 | -44.4909 | 2024-12-13 03:55:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4c3821a-2c57-3b58-9d64-0dfde2bd58a1 | -7.26021 | -35.14905 | 2024-12-13 03:55:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a627828-8938-3502-bf8f-4d5c12ed23f5 | -6.93169 | -43.53331 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f595df2-3e7d-3c7a-8ed2-3668efb80117 | -8.26982 | -48.03179 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6990b50-59a0-3e80-97d3-41399c545869 | -4.47962 | -48.11705 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d13eab5-b806-3b34-bb32-a80a7c8e99f2 | -9.32337 | -35.58077 | 2024-12-13 03:55:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67f4a982-b51d-38a4-9df3-d2d516627fb7 | -2.57769 | -49.43708 | 2024-12-13 03:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af2c6aae-b62d-387e-ba25-c2d32eed4ece | -6.90794 | -43.55327 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 069e52bf-733c-32ae-9c0a-d6be89b089f8 | -6.3796 | -39.25183 | 2024-12-13 03:55:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7970a4d6-8c07-3462-a6a6-7319e5c18e73 | -6.09001 | -43.53954 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 136b4e45-2f64-344b-819f-dddf111de957 | -2.58398 | -49.43818 | 2024-12-13 03:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ceaca8c-bd0d-3fd5-833d-503a7cc03b64 | -6.09729 | -44.76006 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 98d33d3e-cdf1-35c2-959b-a4342910d108 | -6.92616 | -43.54204 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8881385-7d59-3281-9781-23e4112ca5bf | -5.62364 | -44.83596 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd461d71-ff9b-3683-8e39-054e6e8a2d73 | -3.83303 | -41.56492 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8465b26e-d37e-32da-8d1b-ecaa7c8994da | -6.12804 | -42.54307 | 2024-12-13 03:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2db16d2f-38ba-335a-93e3-28f9e378639b | -3.8316 | -41.57367 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0e4d6e83-61f5-33c0-af95-2af22119909e | -5.20319 | -43.29578 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75480e6-5289-3afb-8b5c-ad88a832ed5b | -6.32315 | -44.7603 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9247bc3-771c-330e-a7d2-04ae001b31ce | -6.56445 | -39.11401 | 2024-12-13 03:55:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 109905fd-b410-381d-b291-a0daf6820091 | -5.45328 | -36.87188 | 2024-12-13 03:55:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 11b3fb9e-1aab-37ee-af25-96d03e4bcb28 | -2.8326 | -40.30405 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 470fcdad-3d4d-39a9-9472-a852d245541e | -6.13435 | -43.95805 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0e22d78-b5c7-3c1d-b220-33de1fdb1c19 | -8.71337 | -44.00563 | 2024-12-13 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca95b66d-a09f-369f-a79d-9638f2426801 | -6.91026 | -43.53942 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2eb87663-a235-32a0-a1c6-b215c45874e0 | -6.93084 | -43.53842 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a699b25a-add6-3843-8f50-d9acb71ad82a | -6.76591 | -44.82442 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5a608079-d203-31d1-a55e-aeb824ab7778 | -8.48189 | -35.38773 | 2024-12-13 03:55:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 47a78459-5876-3f32-a2f0-563e41ed8a38 | -5.969 | -43.36529 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b034ae64-b8e1-3cbe-820f-74ddde79a8a1 | -6.53639 | -44.51908 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38fb90ca-325d-323d-ab00-2bc6371a48fd | -6.93013 | -43.5427 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d061bbd5-6b9d-3ca0-81ee-0a62ccc40d55 | -10.19999 | -36.37115 | 2024-12-13 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bde6f25a-0464-3818-a37a-95a5b84f3d8c | -5.88573 | -35.41637 | 2024-12-13 03:55:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 639cb506-8b6a-379b-9fca-d30a123e1f55 | -7.99398 | -39.43412 | 2024-12-13 03:55:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ddbf3ef-3ae1-3424-92f7-a304c1e30681 | -3.83123 | -41.5574 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00f9aef5-8009-3694-9228-50128db008c9 | -6.91496 | -43.53578 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ea2fbf50-721a-3fd5-94d1-862b8da45025 | -4.51214 | -42.06458 | 2024-12-13 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29e81979-8c25-3687-b94a-6ee5b3c8cec6 | -4.45203 | -44.65441 | 2024-12-13 03:55:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a702f22-7735-352e-a24f-dd2f85f67378 | -3.30758 | -42.74157 | 2024-12-13 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e0c1681-58ec-327c-9dce-4d939cbfd84c | -6.09658 | -44.76432 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b45970f-68a7-30bb-ace0-d0562425dd9b | -8.80871 | -37.12132 | 2024-12-13 03:55:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f93b9eaa-dac0-35b7-ba27-a8b596865ab5 | -1.62359 | -46.66656 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ce23ac1a-ce71-3287-9028-edaf58449192 | -7.86854 | -35.48716 | 2024-12-13 03:55:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c7661a64-4fd5-3564-89ea-025d1b9c082d | -4.96996 | -44.96513 | 2024-12-13 03:55:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d6a69e2-8134-3811-acef-4b26150aff47 | -7.42994 | -44.73579 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a4c0421-5e3a-3d18-a18f-3128536e84ca | -7.43781 | -44.74121 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7237ef6d-3163-39fa-80cb-2e1d70411a02 | -6.91098 | -43.53513 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 771d697f-101f-39c6-a774-2abfb5fe0c08 | -1.6177 | -46.66903 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c01b84c9-8a1b-3a83-9613-eb3d15bcdd9e | -4.81168 | -44.47437 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a62143a-504f-39a9-a8f4-07eeb19e9746 | -6.20907 | -43.27771 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb858cdc-4068-393a-9c87-20ffa3da649d | -8.549 | -40.68931 | 2024-12-13 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b38ee43-03e2-37d4-affb-f14505b2894a | -8.2704 | -48.02848 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb94f2fd-1a48-3e5b-a3bc-58574a9f1772 | -6.94677 | -42.85693 | 2024-12-13 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dce2f15b-053e-35c1-bfb9-c8a5aa88a856 | -6.9215 | -43.52102 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 99fc7d68-690d-3414-a977-fcb887a2b7b3 | -1.89952 | -46.81992 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f0702a1-ddb1-334c-87ae-1992c821b3ff | -3.3608 | -42.27797 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc4dde8e-813a-33d6-bd9a-d84a2b8f7f07 | -6.91979 | -43.5313 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bc074f98-a2c1-3381-8d5e-dfad1c56e02f | -7.29123 | -45.08284 | 2024-12-13 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a715f91e-9ca6-3862-a763-2c8728f9f2f4 | -3.83444 | -41.55622 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1983f784-1682-3939-944e-6175eccc34d6 | -4.6511 | -43.81624 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aebc283-968d-38f9-af49-4e361db06943 | -5.93733 | -39.85764 | 2024-12-13 03:55:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88233222-7952-34f1-8fab-99d0811bcdd4 | -5.39136 | -40.66235 | 2024-12-13 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f49547c-b0ff-3a7c-839a-7a7c0a27a531 | -3.00384 | -40.22738 | 2024-12-13 03:55:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa748055-7db8-35cd-9813-649790b849c6 | -5.05999 | -44.23312 | 2024-12-13 03:55:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 277b0ff5-2807-391e-a2e8-a3dc45ad2527 | -7.25151 | -39.85041 | 2024-12-13 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65e9a813-0e1b-38b7-a7b2-46f02ce780e2 | -5.94366 | -43.7708 | 2024-12-13 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd9b673e-7da0-360d-806d-1bce0da596d4 | -1.57334 | -46.03999 | 2024-12-13 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f65fb27-9da6-31bc-bef4-916c51f598f9 | -4.78205 | -48.50397 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c6b8113-b3fe-38c5-95a1-ebd75df47ced | -6.49279 | -44.10843 | 2024-12-13 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 239caa45-c863-327a-87e8-7819794b7d75 | -1.53302 | -46.29486 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 381c7e3d-fc0a-3611-a28f-bd9ce31077dc | -5.21583 | -43.2941 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| af9a741d-a199-35a9-87b8-ee1dfb24cf47 | -8.27093 | -48.02432 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35a11043-1384-34c3-a856-ba12989e74b8 | -2.83207 | -40.30062 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ab2198f-5ea8-39a8-9b35-7c01191be625 | -1.46477 | -46.81019 | 2024-12-13 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edb11126-5cf6-380c-bc22-3c029080b9fe | -3.04053 | -44.47395 | 2024-12-13 03:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af09c010-bffb-3022-98dd-919a8fd1e89d | -3.68722 | -42.6017 | 2024-12-13 03:55:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf5a6e48-e84a-3921-a745-d71aed121edc | -5.21238 | -43.29006 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 4a86ccc4-703c-3fc2-a657-585f4505c55f | -6.9341 | -43.54336 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23212238-a6b6-3340-aab2-1978ae9217cf | -8.82343 | -36.5597 | 2024-12-13 03:55:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41dc446d-249c-3160-a7af-547a198b1250 | -4.51285 | -42.06002 | 2024-12-13 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c9e3ae29-f7ac-3b1a-a93b-776384724b67 | -8.4841 | -35.39017 | 2024-12-13 03:55:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8382305b-aab6-3116-b6e2-5899bb473907 | -3.68403 | -50.23861 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c0ba48b-e500-386c-93b6-5efb223f067a | -3.25004 | -42.41765 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aa25551-6085-3afd-94c9-817bf20ad965 | -4.65048 | -43.82006 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 076b437f-3c26-383b-a2ce-c598c89af7e4 | -6.92772 | -43.53263 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e742f6c-49e1-306b-a48f-ed6041d10cd7 | -5.96502 | -43.36465 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d70a6a28-33b6-3ac8-a7f6-4887098e669b | -6.73716 | -38.15974 | 2024-12-13 03:55:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fdc1afcd-0add-3d51-8624-914256564364 | -7.42927 | -44.73471 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README13.md)
