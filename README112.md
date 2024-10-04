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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd043d33-9ac0-366a-80a5-0d742d60f6fc | -21.83648 | -48.38342 | 2024-10-04 04:34:00 | AQUA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 4ad344a7-14cd-3607-b6c5-0aeeb5f97454 | -21.78609 | -48.37412 | 2024-10-04 04:34:00 | AQUA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a667c01b-25a2-32a9-ab51-f0c1d76a48f6 | -21.78477 | -48.36886 | 2024-10-04 04:34:00 | AQUA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 6234dc78-ed32-3484-8e5f-261be6dd1362 | -13.89127 | -44.27711 | 2024-10-04 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c53b4b-b864-36f2-a5c3-55b3d75f2ed0 | -14.50482 | -45.21684 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34bb3a9c-66a3-3a41-9822-7e536f195272 | -14.50869 | -45.21751 | 2024-10-04 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50747388-d65d-3839-9826-fa77571c55d3 | -13.5003 | -48.63278 | 2024-10-04 04:34:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 445db394-bd0d-332f-8995-493c4d016b55 | -17.8543 | -41.42399 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe66aadb-15ad-33fe-969f-15bc27271bdf | -17.85418 | -41.4244 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7dbe6129-e85c-35e0-8be8-cebae7363b62 | -17.85395 | -41.42724 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66d93025-ec80-353c-a56d-e223de0cdfbe | -17.85381 | -41.42761 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c4fba460-5361-39d0-9649-835e54325891 | -17.85363 | -41.43029 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 199faa85-f5e2-3330-bea7-6cf407bffee3 | -17.85346 | -41.43066 | 2024-10-04 04:34:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4250c97-6141-3514-889e-c74a9bc200d1 | -16.89773 | -40.61116 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4603a4d3-2560-3704-afd0-ec0cec844485 | -16.89733 | -40.61462 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bdd5321e-c568-37e1-8bd2-6fa580ea8393 | -16.89348 | -40.60932 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c037de1-2eb2-3666-9b0c-afdd3d64c2f1 | -16.8931 | -40.61285 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f2c1e5a-a5ed-325d-a28a-e6f15f39f946 | -16.89231 | -40.61041 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a71d0fb-2a6b-3e95-b022-e7ce8e9cedc3 | -16.89191 | -40.61394 | 2024-10-04 04:34:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b24bacb2-2da2-3000-80d2-b9a035dadeaf | -18.51005 | -41.29727 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3b2901dc-edc5-3521-b197-067447a56464 | -18.50967 | -41.3007 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 276b9ac3-7a65-3b19-8db2-71dacd864999 | -18.50929 | -41.30407 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e88e440b-3601-3ef5-9c13-7bb4c5a7c7d4 | -18.50834 | -41.29642 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6fb531c2-4c82-339c-a2cc-461d5fbee050 | -18.50799 | -41.29984 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 08d4e73b-687e-3e36-8d8b-a85339d2cb0d | -18.50764 | -41.30321 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e5e128b5-c8aa-35df-a413-8f2b31b33ae0 | -18.5044 | -41.29984 | 2024-10-04 04:34:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aa63c9c3-c42b-3de9-8b83-7e1232c05b4f | -14.77294 | -41.61695 | 2024-10-04 04:34:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7539ea3-8d35-3476-a098-06d57a810908 | -13.87826 | -42.01852 | 2024-10-04 04:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccf6d9b0-ce9a-3c37-84b6-462004ac6a0d | -15.43451 | -41.14096 | 2024-10-04 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d1a47033-3ba3-3d51-bbfc-b6f1320d7237 | -15.22705 | -42.16354 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c8845aab-98f0-3483-8c5e-b76571daa613 | -15.22642 | -42.16422 | 2024-10-04 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e775afa2-08b1-322e-91cc-38686139766e | -17.3792 | -42.62428 | 2024-10-04 04:34:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1dc905a1-eec4-3bb8-803f-a52c668da36a | -17.36966 | -42.62299 | 2024-10-04 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0567f676-e24b-3ade-942b-03d273ab201b | -17.36425 | -42.62765 | 2024-10-04 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d325e1fc-c18f-30f8-bfe4-b4704450ac17 | -17.36902 | -42.62831 | 2024-10-04 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6bf2489-7542-3757-8d6d-4cd10a9d1972 | -17.37443 | -42.62364 | 2024-10-04 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2221c112-f1b1-331f-8697-a5fcfd42eb36 | -17.37379 | -42.62895 | 2024-10-04 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 474ef55e-05a6-3425-8e53-495fa75279af | -17.93069 | -42.20821 | 2024-10-04 04:34:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c107c175-00b3-3609-bb79-68723f758b24 | -17.90794 | -42.1875 | 2024-10-04 04:34:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e1c5132f-abc7-33a6-ac02-7c5eb0422fa0 | -17.84499 | -42.06936 | 2024-10-04 04:34:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9257ec6c-5688-3ab4-9c93-828419ecfd4b | -19.51041 | -42.323 | 2024-10-04 04:34:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab7b1dae-575f-325d-ad72-ea472cd5078f | -19.5099 | -42.32767 | 2024-10-04 04:34:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f0dc4c5-fbcc-30e3-96c0-414b0fec23fb | -18.0842 | -42.59497 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e5048f4c-9673-34b0-9c93-f9065aa0f8f7 | -18.08354 | -42.6007 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 959431fb-797a-3c73-be7e-c619ffeb7252 | -18.07936 | -42.59436 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 06fb1ce2-be27-39f4-81e4-24d39ea81dbc | -18.07871 | -42.60009 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 404c6ce7-a788-3b12-9735-508be2b2081e | -18.07453 | -42.59375 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 15d03cc6-ca61-3aa6-a943-eed4505ec595 | -18.06905 | -42.59887 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 42998aac-91b5-3772-9c58-b9e5efceaf3c | -18.06581 | -42.62728 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c18f65ca-2f4b-3d3a-9369-595e37fc836e | -18.04387 | -42.61287 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a40f8c4a-71e7-3b16-a72c-176d084bdd99 | -18.04288 | -42.61382 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3d11c9cb-b701-3142-9b9a-58fc771d2f69 | -18.03903 | -42.61241 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8346f5d9-ff0c-309c-84c6-5be33cd1be98 | -18.03805 | -42.61334 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a0d245af-190e-3f00-b1fb-646f1e643af3 | -19.03086 | -43.18577 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fee6fdf1-e0c4-3382-96e8-6347df093170 | -19.03026 | -43.19084 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5cad5bd9-e30f-3bde-88c4-7fa819954242 | -19.02613 | -43.18541 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 311db1d4-6182-357e-965a-6c2039c93336 | -19.02554 | -43.19034 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| cdf7b688-7ba1-3757-93e6-7417d613ccec | -19.02496 | -43.19528 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5ffcae44-1762-39d0-bc15-f4871122c16e | -19.02438 | -43.20015 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eceb4c31-9745-33a1-b8a8-f53599e11243 | -19.01726 | -43.17962 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 38a37dfc-65a6-3965-979b-51a363475314 | -19.01254 | -43.17916 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| fb71b6bb-31d0-36d7-8c64-302ae96ed3a8 | -18.97639 | -43.20285 | 2024-10-04 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7c20f938-9769-3696-a89f-b44b3eb29df3 | -18.97581 | -43.20794 | 2024-10-04 04:34:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3fb1e739-893c-35e1-b58c-cdc4eb2f538f | -18.97227 | -43.19731 | 2024-10-04 04:34:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a7a773e6-934f-3cbb-a2bd-c75e4921bff4 | -18.97169 | -43.2023 | 2024-10-04 04:34:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7313f57c-c6ce-3627-a59b-0b1cd6e59d9e | -18.96995 | -43.21741 | 2024-10-04 04:34:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4174e4fe-671d-34f8-acb2-fab38af9ec5e | -18.86359 | -43.13652 | 2024-10-04 04:34:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2e602563-4a96-38fb-a74d-9fa669264669 | -18.86014 | -42.9112 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bc0ecbe2-97c2-3109-ae28-6d130b934fc5 | -18.86003 | -42.91237 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d4cc7828-d7b5-38d8-aaf3-4a2f97fbd956 | -18.85954 | -42.91622 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9db25df5-2868-3003-906e-6048e9a954f6 | -18.85594 | -42.90569 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 24a3aea7-9452-3d5b-aa27-0cde92f8a433 | -18.8558 | -42.90681 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d6519537-0bac-3fc6-92d9-7682a71a19f7 | -18.85534 | -42.91071 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e67f3e37-1df1-3278-b0db-34b015f14d2e | -18.85524 | -42.91183 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a7568518-5d68-3aa2-9cb7-4cb3c616b4d0 | -18.85476 | -42.91562 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 97e36b69-ab7c-389f-a0df-d005239dbafa | -18.8547 | -42.91672 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 27f6eeb5-bbb3-3ae1-8194-11bd8494e8d9 | -18.85161 | -42.90085 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 27cfebab-e157-39f3-b1e7-4171c13bb331 | -18.85118 | -42.90491 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6d530dd9-3c5e-3110-bb3d-6eda9dbefe21 | -18.85103 | -42.90608 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3b1a7810-1de5-38a8-a620-0ec38e9c95e9 | -18.85055 | -42.91027 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b1f25092-84db-351f-9a19-8ea51cf68085 | -18.84578 | -42.90961 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| f8961092-a1a5-3283-96cd-37240f84acc9 | -18.84108 | -42.90833 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 2317a4b0-2384-392a-8024-d78c0404e560 | -18.8404 | -42.91413 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9dfd2996-9101-3286-a2ff-f82862fa990f | -18.83776 | -42.9776 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bd3d1311-87dc-3466-bd40-7e2cb0570c98 | -18.83569 | -42.91297 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 454a8562-37ee-3e5b-b278-91c2666b9aca | -18.83506 | -42.91837 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c788e28d-d5c8-383e-a49a-69f3f26c9cf7 | -18.83299 | -42.97715 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 816f9585-e277-3d17-aeb1-1a9ad68e5bac | -18.83175 | -42.98762 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b44e9308-4a97-38b5-a427-7eb3ed3e1eb1 | -18.83035 | -42.9172 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a54d62b9-1286-33f3-a4ab-f3b7d00a9fbe | -18.82821 | -42.97669 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b4ee2727-b713-30d8-8f37-ba9d3fd13624 | -18.82698 | -42.98722 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e75b7181-5147-3afe-a0c0-66b55f5dab6c | -18.82222 | -42.98669 | 2024-10-04 04:34:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4b27b3df-dc2c-3a13-b62e-1bcd942e3638 | -18.69384 | -43.05373 | 2024-10-04 04:34:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 616234e3-7348-34c6-8c22-6c7eae270824 | -18.57813 | -43.04804 | 2024-10-04 04:34:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74779988-c509-3a8e-b4b2-830b2f4d3098 | -18.57341 | -43.04742 | 2024-10-04 04:34:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b610229-dc22-37d0-b72d-630a7e6c4976 | -18.51015 | -42.96806 | 2024-10-04 04:34:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3ecb23a-639e-3ee9-8ce3-8911195a96f6 | -18.34695 | -43.03959 | 2024-10-04 04:34:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e4b3ab7-f201-3656-ab0d-470b5b7d20b3 | -18.06095 | -42.62705 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cea7b4f2-6b2e-3501-aab4-2f0442aa48b9 | -18.06034 | -42.6324 | 2024-10-04 04:34:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d09a328f-7857-35b6-a314-697ac85d8bd4 | -19.32552 | -42.58767 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |


[Clique aqui para ver as próximas entradas](README113.md)
