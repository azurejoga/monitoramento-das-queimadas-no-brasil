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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f924f8e-21cb-39f6-9ac2-bf460e61a22f | -14.61376 | -46.37442 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acaad117-9164-3ac0-a3d6-b79b01fdc6e7 | -13.62844 | -45.37165 | 2025-09-17 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d2dd4ad-1ae8-32fc-96b6-295632fe6dbd | -12.36663 | -43.20509 | 2025-09-17 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e0ee0d-11e9-31ce-a14b-358895d2c4c2 | -14.60385 | -46.39712 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b59c5943-f9e5-310e-a463-c41b08a0be7f | -8.96406 | -45.75382 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea93d277-faef-32c9-8f01-fa78999421fe | -8.57204 | -46.34103 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5f33ca5-0fab-3d9c-8c39-3fc37f49c7bd | -12.72145 | -48.01273 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e3d3e79-ef2d-3b94-8225-f4057bb1f803 | -12.28131 | -43.82498 | 2025-09-17 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5a662eb-75fd-3711-bdca-45bcdd6609de | -14.26915 | -44.68119 | 2025-09-17 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fbf347f-4ab6-3a12-a6d7-dcb42954476b | -8.98619 | -45.75786 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8e3d311-d5d0-351b-9ac6-395fbc59fe2f | -12.06771 | -46.53946 | 2025-09-17 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 719eb847-8a9a-3c77-85ca-b4664fa9e09a | -8.9741 | -46.0114 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c584801b-658e-32fe-960c-5f780ed400ba | -12.72742 | -48.01392 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13041e7a-1b58-3125-b7af-ad45c8bfbd69 | -8.56171 | -46.36456 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32903200-bf45-3486-bf6f-feda0334fcca | -14.62102 | -46.39252 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cac5b323-e86d-3af1-932f-c4cb7bab7bff | -12.7295 | -48.01691 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb4d90a-646b-340e-a469-bec3ee79083c | -18.33268 | -43.29549 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c421e1f9-b44e-3a99-8807-a7b3729c3884 | -15.39505 | -46.14222 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 532c36b2-14e7-3c22-a19c-e3994da49821 | -24.7599 | -51.99138 | 2025-09-17 03:47:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f1206839-9812-31ec-896f-e486c2facd80 | -19.10685 | -47.14009 | 2025-09-17 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80d9b855-a6ec-3dd5-8ac5-cfbb861f990f | -14.808 | -51.71158 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e8531a75-3205-3c62-85eb-97324e13840f | -15.39778 | -46.12855 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83ebe9fb-daa0-3de2-8c33-f2f75a1bfa62 | -15.41619 | -46.14163 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b797c4-03e0-3f2c-8e9f-8b242e722982 | -17.3307 | -46.80876 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e0f83f-ef1d-3c33-af76-72e1de78c684 | -15.98716 | -46.44804 | 2025-09-17 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c48ff371-084a-31b7-bc39-8121dda4b576 | -15.39887 | -46.14942 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2143e24e-05c8-3186-bfc9-8421f74319a7 | -18.17555 | -45.17884 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a94b440d-3c6e-30a4-a01b-919ed06c32a8 | -20.4302 | -40.74649 | 2025-09-17 03:47:00 | NOAA-21 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0a863fd9-8a00-33d6-b64a-59b68dd415cf | -14.80219 | -51.71827 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| de4ccac9-8edd-3b5a-9b66-cdbe9185d2e9 | -16.11339 | -42.61353 | 2025-09-17 03:47:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 544131f3-67ea-36f8-bfbe-53e7500d7e05 | -14.7037 | -50.24636 | 2025-09-17 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 54ab223e-35f4-3e65-9bfd-008575b065ae | -21.97882 | -47.96302 | 2025-09-17 03:47:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aad64541-20ca-36c4-a7e2-21c5820b21e9 | -17.80759 | -41.49844 | 2025-09-17 03:47:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23774add-6634-3193-85ff-4f43b05dbb3d | -15.41295 | -46.15797 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd5b16a5-76b6-3732-85f2-c5b0f7060813 | -19.53326 | -50.59433 | 2025-09-17 03:47:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 442ae6a7-e34f-3d2d-90f9-06bc42856a63 | -15.41676 | -46.13875 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 255c3ffb-cbfe-35a4-bf40-e1cfd76cf774 | -17.57179 | -49.06911 | 2025-09-17 03:47:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5177db1-4c03-334f-b690-96736643e69e | -17.23959 | -43.43569 | 2025-09-17 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60c755e2-f747-3bf3-95cb-f069c3243eae | -18.32796 | -43.29863 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| f4fd6f57-7f7d-3f4e-a9e0-f497581d1ffc | -15.41998 | -46.14901 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9171c82a-1e65-3540-a1f4-46bb0ef2528d | -15.42057 | -46.14602 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edfaa7ca-bc83-3ece-93af-43ce339f0921 | -18.16741 | -45.18988 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9090168-2107-3191-b858-31dfb2989588 | -15.55284 | -46.7109 | 2025-09-17 03:47:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9fec83d-b448-36d0-bf77-67c964c7bdcd | -17.11839 | -43.59346 | 2025-09-17 03:47:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8a9089e-3b90-3a87-92ce-83d61de69157 | -18.32649 | -43.30647 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 92997441-9f19-3d15-905e-d18559d49052 | -15.41225 | -46.1615 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 322a6978-5aa7-36b1-b0c1-5535e9fac094 | -17.0453 | -45.89045 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1eb40a4d-27d2-3815-8e14-0a728fe5b74f | -17.93751 | -45.25291 | 2025-09-17 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b37bcecd-02c8-35f4-8b0f-eaf235955a23 | -18.36728 | -43.30965 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bcf14a15-0778-3b6b-8104-6321492dc861 | -18.19877 | -44.55064 | 2025-09-17 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23a087f9-6dd9-3091-8ada-af8d94161971 | -16.61421 | -43.36824 | 2025-09-17 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a729433-57bb-3f2a-8bf7-0af864474142 | -15.41365 | -46.15444 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff224560-cc0b-3df3-94f8-b3fda6d335dc | -18.1918 | -44.54021 | 2025-09-17 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2d9adbb-378f-30c2-b295-da9367015234 | -17.32877 | -46.81816 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aa40955-a4b5-3ddf-912f-5e0b3a25d2d6 | -17.96762 | -45.24418 | 2025-09-17 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb2c0bd5-3a3b-3b1f-a3cc-4f9bea4e05c3 | -15.42048 | -46.11994 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5747a884-fa81-3747-9dd6-d8f156abeabf | -17.34093 | -46.81057 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7db6db6-1758-34b5-949d-4cf8d877d060 | -15.42113 | -46.14318 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8af6bdbe-a666-351e-8c45-23940f397a18 | -16.40279 | -40.9405 | 2025-09-17 03:47:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ea81022-3e4e-392a-bd6f-e89433071903 | -18.17291 | -45.18565 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71db393f-01d3-3ccc-b49e-743a610c49a2 | -18.32573 | -43.31049 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2c63ee73-4473-3159-a313-b75a7cbb53e7 | -17.33521 | -46.81261 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cea50251-0ea6-3bbf-be53-1d50cac1af27 | -15.98595 | -46.45403 | 2025-09-17 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ac6eaef-bf87-3e16-a86f-6050f698285d | -15.40717 | -46.16061 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8ab3a43-6fef-3a01-8b24-883436504ba6 | -17.31786 | -46.81961 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72b24fbc-698a-315c-8d41-059a21cc305c | -17.96516 | -46.00473 | 2025-09-17 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b373198-4dbe-397f-971e-59e23db96c8f | -17.56231 | -43.79196 | 2025-09-17 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce6281b5-197a-3381-9db5-e0692efe6e41 | -17.32811 | -46.82138 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dda9d76-11c1-3cf0-9293-1ce980793190 | -18.19792 | -44.55501 | 2025-09-17 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aee173f-7a17-3933-b5ae-c610772a0ffd | -17.72301 | -43.56622 | 2025-09-17 03:47:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c5ce430-1487-30ad-a41a-5997bbef84ed | -14.91116 | -51.69783 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8889ace5-4fbd-3dac-aece-34e4e6706c79 | -15.40169 | -47.35209 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffa5b52f-8aad-3a76-abc9-c9cb3ad893e6 | -15.92964 | -42.6393 | 2025-09-17 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8062344a-98dc-370a-9794-3f2c6a54b7ba | -15.42497 | -46.15034 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 345581d9-7be1-3cf2-81a8-44b88e76e6ab | -18.08593 | -42.77132 | 2025-09-17 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc50a53b-8540-3c14-a6eb-3f981fde9c57 | -18.25086 | -43.32697 | 2025-09-17 03:47:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5f22c94-62d5-310e-bb18-1290c7d20f97 | -18.17382 | -45.18087 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57ab7389-d190-38f4-ae10-5ebe6b373ec9 | -18.36942 | -43.32048 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 859c20f6-d5fb-3b0d-a5ef-fe89efe6abaf | -17.3391 | -46.79362 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf48bb01-02eb-3947-b7eb-9985a41b971a | -14.80092 | -51.70992 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 192d5ae4-8795-3ee3-b4ed-0bcb136faecf | -17.57276 | -49.06474 | 2025-09-17 03:47:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b89179f-ee3a-37e8-aad6-956fe44dfca3 | -17.19395 | -45.91795 | 2025-09-17 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11f66d9e-67b4-3dbe-af06-d06f77abe5c4 | -17.32496 | -46.81086 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46ddabaf-038d-38f6-91ec-37375456f444 | -18.52381 | -48.1497 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86580741-8701-342d-83c1-c9ce576db06b | -15.40016 | -46.14298 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ef1996c-4dbd-3c7d-920c-699fa5ef8bfd | -21.42216 | -45.46898 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c2b70654-89da-3d41-bb44-acf3aab58582 | -18.37005 | -43.31708 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d85a19e3-2028-30bf-a663-0e8729ac2d36 | -22.2032 | -48.35463 | 2025-09-17 03:47:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c0c90b-03f7-3e2e-acb0-092937a3f310 | -18.4988 | -42.69818 | 2025-09-17 03:47:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 128ae6fb-bc05-30a7-ace7-09f0f607751e | -18.36668 | -43.3129 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2c8518d1-6180-33ac-84d3-cc74435d0a54 | -17.04418 | -45.89594 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4940ab88-803d-3c8f-8630-d0678befe680 | -17.943 | -45.2491 | 2025-09-17 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4426b122-a491-3334-8d75-8a908d3dd36d | -14.90954 | -51.70502 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5e0408e3-9ae1-36f2-bb7d-570c0ed70756 | -18.35739 | -43.31842 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| df2fb5e5-fb45-33f9-aa85-523efceac119 | -17.04569 | -45.89463 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e041e09-3d8f-3aae-a5cc-b56ac9c330bb | -18.19031 | -44.5405 | 2025-09-17 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc4c97c0-3994-3469-b70d-965df3c74b87 | -21.56526 | -50.12634 | 2025-09-17 03:47:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 820bb82b-29b8-395f-a564-e760de0e9482 | -18.3567 | -43.32212 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69e6c9e1-e2e5-3931-b8aa-ed86af340b51 | -15.42441 | -46.15321 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f75841e-05c2-389c-82f0-819baa94849c | -24.75764 | -51.99314 | 2025-09-17 03:47:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
