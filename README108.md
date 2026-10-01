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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82620b6d-aa9d-32d5-9360-bd2a9028b661 | -18.97583 | -44.37307 | 2026-10-01 16:09:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 43.9 |
| e74e61c1-aa02-31c9-a857-73349f4bc4d3 | -16.25797 | -41.3237 | 2026-10-01 16:09:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ee172d49-3711-3171-94fb-c71550e01794 | -18.76909 | -47.61163 | 2026-10-01 16:09:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b399b1f5-63e1-3b09-b09d-888d0fdadc10 | -18.33778 | -40.05594 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5f7a9f83-c2fb-322b-80ef-0a0e23382adf | -18.20358 | -42.31781 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| dac1e3a9-719f-3450-be08-d4430331e029 | -19.04533 | -45.6621 | 2026-10-01 16:09:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43d31515-c96f-302e-be20-2df3321d8dc3 | -18.82975 | -47.42334 | 2026-10-01 16:09:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7452f90e-0e61-3c3d-b459-5dffdd410af0 | -19.77351 | -42.84407 | 2026-10-01 16:09:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3b722885-2634-37c3-8a32-febe10b062dd | -16.31423 | -40.1297 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 81c7523b-d4e2-3542-a45c-41b3a51883a1 | -17.58673 | -46.79387 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e2c12f9b-4a97-3834-b48b-2e184097e1bd | -17.89195 | -42.22423 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 75a6c5c4-baf4-37a9-9d4b-c948a1e776df | -16.86798 | -39.26231 | 2026-10-01 16:09:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 873e2383-d861-3e7d-ba4a-853c5198908c | -16.35596 | -42.58207 | 2026-10-01 16:09:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f09d44a5-41ac-3103-ad79-7e32314e3e19 | -16.99712 | -45.47008 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 430b2c5a-160b-38f9-9863-904d69674d9f | -19.37376 | -42.26325 | 2026-10-01 16:09:00 | NOAA-21 | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 884c47b9-876e-3899-be58-3e3ae92c8b4c | -19.13711 | -40.66347 | 2026-10-01 16:09:00 | NOAA-21 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d92ded1b-b1d5-343f-8253-752dc5fbe3b8 | -20.19061 | -42.44088 | 2026-10-01 16:09:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8c15517d-aada-3b59-bb3f-c8e77afeeb7a | -19.68064 | -40.93789 | 2026-10-01 16:09:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 621677a9-f127-345d-b8a2-3b7cea0b09f9 | -16.90288 | -42.10311 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 36cedc09-daec-3b55-82a7-88aa0b063200 | -18.74278 | -43.40192 | 2026-10-01 16:09:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1742b571-ce16-3e6d-8ee7-911edda08cf8 | -19.34283 | -41.45024 | 2026-10-01 16:09:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| c695faee-6b28-37c4-a544-fdc3aec6fbc0 | -18.20125 | -42.97383 | 2026-10-01 16:09:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9ce6069f-fc7f-3a53-bc25-d3fb183421a8 | -19.12143 | -40.35304 | 2026-10-01 16:09:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bfbc4e03-f6f1-3503-a34c-dd93244bac28 | -16.35714 | -41.908 | 2026-10-01 16:09:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| e01335d5-25c4-3634-8132-ce5ebd4e2aa2 | -19.82319 | -45.85397 | 2026-10-01 16:09:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c875a3a7-b192-3faa-b9f1-c67b9bb0b33b | -19.62776 | -47.17577 | 2026-10-01 16:09:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a79183e9-5ce8-31a1-9c8e-3429ee3d9eb4 | -17.91341 | -45.05678 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 095a1347-22de-374c-be28-24cabc31f053 | -18.55178 | -40.13927 | 2026-10-01 16:09:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fbca6327-737f-393e-902a-5fe436e8b3b9 | -19.10285 | -44.46263 | 2026-10-01 16:09:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8532c05-137c-32e4-b85d-6464898b752c | -17.88831 | -44.31179 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f8aa1f1-18c8-3b89-b35e-41613c977aec | -18.10743 | -44.55212 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08f5ea33-8513-381f-8f8d-3b7a85d7c276 | -17.81032 | -46.95392 | 2026-10-01 16:09:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d46312f7-5968-3aaf-a581-bc8e960ea76e | -16.90768 | -42.11131 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 76a3d7a6-8157-37b4-b93b-78ba99499c7f | -16.85447 | -45.44149 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 05fcebfc-41cb-30c0-8b42-665da1c3a0b6 | -15.93745 | -38.94999 | 2026-10-01 16:09:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 60193b94-e85a-3c6a-9adf-0abb4eb63d92 | -16.84746 | -41.87419 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 368a506d-3f7e-3f31-8377-529ee7bea28f | -19.22913 | -40.0773 | 2026-10-01 16:09:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d69c07f1-83e4-3659-a1aa-0787f1770b3c | -18.10843 | -39.82623 | 2026-10-01 16:09:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ebdbf69e-b4e6-3b04-8ba1-232ee8ef4c40 | -17.4552 | -44.39224 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c771148-0073-3fa2-80ee-b668e5a7a550 | -18.20421 | -42.32246 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| dc190e41-b473-3d95-acaf-bfbfb7b83967 | -18.92273 | -46.90456 | 2026-10-01 16:09:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aeaa8afe-6f3a-35f4-8dd2-259f0e150bd9 | -18.58902 | -43.55335 | 2026-10-01 16:09:00 | NOAA-21 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| ed650eab-7ad0-3596-92a8-d6252f1c85d4 | -16.84805 | -41.87838 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4a5d6cca-4e86-3076-a55e-b6d09b82a6ca | -18.13131 | -42.78487 | 2026-10-01 16:09:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| f72a5b72-fe34-3532-838e-4b425bb2403e | -17.62583 | -44.33981 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a7d813b9-4e57-341d-b16e-e7ccbabd89ac | -16.83266 | -40.76278 | 2026-10-01 16:09:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0fc3712d-f076-3a5d-8fdd-15ade5df0685 | -17.41393 | -41.11804 | 2026-10-01 16:09:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ad370130-5090-3b6d-b4e6-293128815a63 | -16.85891 | -45.44101 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 97cf6d7b-1e87-3315-9720-d7ed9f653e8c | -19.62809 | -47.17879 | 2026-10-01 16:09:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 80920af8-92fa-39e8-9700-cbfa64910fbf | -19.18402 | -43.95688 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 046120c9-9d01-34a0-8dba-1ef1678cd127 | -21.33792 | -47.19066 | 2026-10-01 16:09:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 00bda376-6aab-32b5-b8cb-9f81e98d9e15 | -16.90229 | -42.09871 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 9617a7a3-2401-3a65-b3f8-39e611a37037 | -18.0591 | -42.38482 | 2026-10-01 16:09:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7c7a5299-3eb6-3b67-bdb4-5b95eb660847 | -18.34455 | -40.05487 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| d2a42306-29c5-31ab-a8e0-bd1b68215429 | -18.12749 | -42.78531 | 2026-10-01 16:09:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| f03d656c-333e-308a-af98-5cc08d9d993c | -18.24113 | -42.07328 | 2026-10-01 16:09:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 96910047-3c34-3a14-aca6-1d6f2887bafa | -17.84709 | -42.21973 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 68a2641c-e123-3f85-a430-0b6aeea71e2f | -17.33256 | -40.7356 | 2026-10-01 16:09:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8ce7b2c7-136e-3d28-9322-82a4b91295db | -18.68164 | -40.06462 | 2026-10-01 16:09:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 71681eea-74de-3ac5-9a7a-b5d8c93cbd66 | -19.72543 | -43.24613 | 2026-10-01 16:09:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ec5402b4-5f5b-36a4-9476-cc8f8295567e | -19.41103 | -47.23988 | 2026-10-01 16:09:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc0a1ad5-57ce-3904-802f-d9093c844d6c | -19.14093 | -44.20958 | 2026-10-01 16:09:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e70c54c-b42a-320a-8f51-0858afa1a6df | -20.62954 | -43.14828 | 2026-10-01 16:09:00 | NOAA-21 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ccd5a49d-bb81-3a65-9c1b-8e00efd2d15b | -17.7058 | -44.3364 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 3349073a-53bd-344c-96f1-b87e49b681f2 | -19.03594 | -45.66217 | 2026-10-01 16:09:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 647232e4-b313-3e2f-a284-436cd80cb7ae | -17.45225 | -41.23999 | 2026-10-01 16:09:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| dbd8ae2f-59cf-348b-9714-5bc42c422e40 | -19.72142 | -43.24657 | 2026-10-01 16:09:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| efb8172d-ae1b-3517-8055-c021233cd31c | -18.27559 | -42.18999 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 24ca4463-be20-3597-a42d-7fcafc0e18f9 | -17.58911 | -46.7924 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 15bd6e27-9fc0-3482-9722-5236bb1a44b4 | -17.88326 | -42.24377 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 582a5bd1-ce97-37ca-9282-0ccf03d6ac9c | -18.10698 | -44.5484 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dccffa48-a260-314a-8939-6c6591723a61 | -20.07267 | -44.59858 | 2026-10-01 16:09:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 55d86719-4199-395f-b485-37a24f6d213d | -18.70899 | -48.83319 | 2026-10-01 16:09:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3aab91b1-24e2-3fd6-ab0d-72cca6cc2fac | -18.83358 | -47.42508 | 2026-10-01 16:09:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| baab1c66-32c3-379d-8b10-27bd8515f622 | -17.09599 | -39.9268 | 2026-10-01 16:09:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 5e9018cd-1fc4-3fc3-a128-d9b88632053d | -19.52848 | -40.19054 | 2026-10-01 16:09:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a415a52-865e-3ce9-a6fc-1269703f843f | -19.66112 | -40.09047 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| f0c46d1c-264e-3054-8615-0f2cfa4e0e81 | -18.94775 | -41.01375 | 2026-10-01 16:09:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d7e61058-ede5-377b-bfc8-abb1f4c98f65 | -18.10507 | -39.82675 | 2026-10-01 16:09:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f2701baa-d53b-38e6-aac4-16d0747298ac | -19.65825 | -40.09491 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 62260430-9e0d-36e7-b95d-b7390b8cbaea | -16.70121 | -40.21945 | 2026-10-01 16:09:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 20f4c39b-da7d-33a6-8940-3da28720ff12 | -17.8089 | -46.95055 | 2026-10-01 16:09:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f16ed3cf-7a34-3d12-823d-26f03dce7e21 | -17.5874 | -46.79957 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 709129fb-bbad-3a1e-a9bc-80db91a02999 | -17.62121 | -44.33661 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b44161e7-2940-3b2c-8823-df62e8fd0576 | -20.77174 | -43.82521 | 2026-10-01 16:09:00 | NOAA-21 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 081376a2-551d-38fb-a321-219bffc7af85 | -15.81721 | -38.9188 | 2026-10-01 16:09:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 842aa0cf-8972-3700-82f0-e2bccb53c933 | -17.7063 | -44.34036 | 2026-10-01 16:09:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6f9db8e0-8515-39a9-b1e0-d2ad319faa45 | -16.85835 | -45.43649 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6ba87165-dd80-3b7f-a3df-a7cc6fdeff10 | -18.40368 | -43.0346 | 2026-10-01 16:09:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| eb8de9c3-4a0e-358b-88c7-976fe54c433b | -17.62168 | -44.34044 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| def22330-2bb1-3d7d-99a7-2cd41a30311a | -16.30737 | -41.88438 | 2026-10-01 16:09:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| cd0628ed-37b7-3e56-b5cb-b712cde6302b | -18.10318 | -44.5526 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 83612c48-c8f2-3678-ba5c-4018ff3ebd3c | -19.28046 | -40.91539 | 2026-10-01 16:09:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1b0c5691-14a1-3449-abbc-0c9aa056b76f | -16.99656 | -45.46555 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 97f625fa-c177-3498-9cbd-737d14b51ef3 | -18.97095 | -41.28893 | 2026-10-01 16:09:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 319a86e4-c0c4-3805-8f86-6c3cecf34a3b | -17.0974 | -46.81897 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1c1aafd2-abaa-3a4b-b737-65565e664d8c | -18.65667 | -46.47078 | 2026-10-01 16:09:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 87cf1912-c11f-37df-97cb-5c2a7e540661 | -19.66167 | -40.09437 | 2026-10-01 16:09:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4a9b776c-6ef7-3cda-a078-20b5507a5fbb | -16.85163 | -41.87787 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 692ac9f4-34e9-383e-993f-b20be15e8f57 | -18.09981 | -44.56047 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README109.md)
