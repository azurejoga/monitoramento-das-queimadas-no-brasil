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
| f4e2d3ff-5c7f-35c9-a152-67972515436f | -12.53547 | -45.80515 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29c97593-6c17-3b23-85ff-2e9dad8d6f4f | -12.86386 | -44.68381 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eb990a7-04ba-3786-8f7d-6751dbd711d5 | -10.38524 | -46.13706 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 327d150e-cd0c-360a-81b6-7f19dc65e32a | -12.05866 | -44.83284 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a474c7-2ac8-3622-a61d-b57057f5a3ea | -11.70027 | -44.3524 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d44440be-71b1-3225-a90c-eff713e56fce | -13.83895 | -45.62135 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 863df870-e93d-32ed-9491-aede8d4b24d3 | -10.80579 | -45.38291 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c19615-a630-3609-9359-3bf4fee86351 | -13.14909 | -44.53502 | 2025-09-25 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b3318b0-ffa2-3044-872d-5a8f0be839f4 | -10.11707 | -45.31094 | 2025-09-25 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91501eaa-ba26-361e-980a-49482897f0c5 | -11.90923 | -44.77637 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c25f0d6-a74a-34cb-8aac-14637c23f86a | -10.57651 | -43.8207 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7af789ed-adbd-392c-905b-d315953da091 | -11.9695 | -46.6067 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fa63b09-e8ff-376f-b301-9fbe1a4c4568 | -8.29026 | -46.0153 | 2025-09-25 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d94d901-8d48-3258-b5d9-20cf9419e42f | -11.66741 | -44.41855 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0decd77f-111d-3443-b109-fa38ce12a3cf | -12.0643 | -44.849 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6b419d-5914-3fde-ba64-b45d427313d8 | -13.83584 | -45.6161 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0584d358-719a-395f-9ede-023dcd9fb9bc | -10.18996 | -44.84167 | 2025-09-25 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fda4510f-3141-30bd-a0b3-5a6f20aa4302 | -8.64614 | -40.39661 | 2025-09-25 04:34:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 379e862a-0be6-3f76-981b-caf27a2251d4 | -10.79245 | -44.43236 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca5b5711-ad4b-3108-8d8e-4b402ba55e41 | -10.39637 | -46.15916 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a239bdd2-31a0-37f8-ba4d-e3c194c470ee | -11.987 | -46.63362 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc1d60f4-4694-35d3-91d8-f9e0baf8c08c | -10.79551 | -44.43117 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 237fadd5-ba4c-333a-b128-7cdd6b253845 | -12.84211 | -44.69635 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5dd7131-9c7b-36f2-8b6c-1557c2340736 | -12.06199 | -44.80872 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e781bcd2-04e1-31b4-89f2-82f7457ab090 | -11.69137 | -44.38785 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fe30c19-5251-3aff-b3f0-d2cca580b79c | -10.17426 | -44.84399 | 2025-09-25 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec82ad65-60c7-30f4-936d-9097c1fae32c | -12.53978 | -45.80128 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46c30913-2c7f-3dc9-91f1-fad75dd63a89 | -11.02153 | -45.91339 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39af73a2-9c0c-34d1-9925-a24960b138a4 | -11.01741 | -44.33876 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62a7d4e2-6c79-33e5-a183-351f667ee395 | -10.84239 | -44.82648 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4ae6bcf-045d-32b0-8b2e-92afe02efe34 | -11.63991 | -45.35734 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32476c99-928f-395b-a32e-ab4b5af1c85a | -8.84789 | -42.47803 | 2025-09-25 04:34:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b8d8a69f-6d92-335f-ae30-3e9386c03822 | -12.84851 | -45.29599 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49fdc752-a5c3-33f2-91bf-4266a7b5e9f2 | -11.61131 | -44.44667 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fab9e12-0d54-35df-bf6c-c8dbf5e78102 | -10.39811 | -46.17167 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44efdda6-f44e-3145-8c3f-67c133958318 | -12.54042 | -45.79688 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf7e2b15-333e-37a8-b4f0-2e91c4b10ff4 | -8.69464 | -44.03484 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6686495-1c35-34a6-a30b-777aece2576f | -11.78851 | -45.56701 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7b11ed4-696c-3b42-80cc-5cc801cc4eaa | -13.84027 | -45.61192 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7040bf06-7544-3ea8-a848-60688e1f0ad3 | -10.8269 | -44.82698 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c52d8365-eebe-3a59-80d9-e71c7fa48b98 | -8.66796 | -44.00105 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8ad952-80e4-36ef-98ee-924c0c6db547 | -8.41953 | -46.92653 | 2025-09-25 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bfcebec-7743-3369-aa7a-ba4fb3e15479 | -12.04693 | -44.86097 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1be3dff2-5cd5-36f9-9e6d-313b9efa3848 | -11.04068 | -45.88207 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ace23984-4326-389f-87b1-4406c73d0a27 | -12.06498 | -44.84403 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c95ae3e-a9d5-3369-9e0f-69554ac2e71c | -11.62379 | -44.44333 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17703e6-feb4-3203-ac4c-3e43d1657e93 | -13.3965 | -44.18796 | 2025-09-25 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 651ccbc9-dd65-3589-bd6b-9f44e12a6b10 | -10.9389 | -44.27037 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2950d18d-e2e7-3f9e-98aa-00528040ec1f | -12.40746 | -44.22041 | 2025-09-25 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4155671f-2e37-3bd3-af8e-130b1d9a0a0e | -13.83453 | -45.62548 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cab4e6c-5e22-3e1e-94a4-ef3a15296356 | -10.76652 | -45.39535 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae7771ac-31a2-3534-b689-3748001b21f0 | -11.64775 | -44.41567 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb93631e-4a59-396c-a9e7-1b4330243a47 | -11.70249 | -44.39472 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef2740d1-be39-325e-aa25-b5207ff5b1eb | -10.58708 | -44.06675 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 081514e9-5dea-3da8-b2fa-a91d550c3084 | -12.02417 | -46.58215 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36838455-1948-33fa-948e-c1fe10029ad7 | -12.86316 | -44.68892 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c924410a-f5ed-342b-8bc3-9e780ceaf652 | -11.66308 | -44.38892 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6ac1968-5f1b-3ddc-a101-0f7f1697bd16 | -12.53611 | -45.80074 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b06cf91-3231-30f7-ac18-559144dd91fb | -11.79762 | -45.58202 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8241722-cf3f-3d71-854d-259897b73976 | -13.83518 | -45.62079 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b88f4c85-29d4-3af1-b7fd-7536f3534ad2 | -9.43912 | -45.58945 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c3988a1-49c8-3ccb-b34f-4970c97a7345 | -12.85346 | -44.67189 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c10f03fa-395a-3322-97f9-ae6cac4e16a8 | -11.47595 | -43.52603 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29f1af22-a280-3ebe-9d1e-fc1ad3c94778 | -12.07111 | -47.98714 | 2025-09-25 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c98c9993-375e-322c-b46c-876d95962bb6 | -12.41816 | -44.75102 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c6fa38d-77c4-3747-89bb-06ad7b6ba9e2 | -10.85299 | -44.80751 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e398ca1-6e01-3838-8a39-2a742941634c | -8.73616 | -45.41953 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f0c5d363-680b-3745-9867-a9a7c7549612 | -10.58781 | -44.06156 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8353517d-15dd-3a71-b9f1-b9960607e09d | -9.43555 | -45.5889 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36e4745a-212c-3080-b8e3-3fdc3190b561 | -10.17358 | -44.84861 | 2025-09-25 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46994ac8-a272-3318-86fe-2818193fed6f | -11.70422 | -44.35297 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e89831de-1593-3046-86cf-848a9046e264 | -8.51039 | -44.9939 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4eecbb8-8d7e-31b9-9fb0-f088d7c402ea | -11.64234 | -45.35514 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c499367c-0a6e-37ac-a472-c8169e72072e | -8.13285 | -44.13581 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4918f6f-2496-383d-99eb-ee80cefae278 | -11.69067 | -44.39298 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80beeddd-95ad-33d5-8c56-a65a87694915 | -11.42021 | -44.92395 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae2c8d61-661e-30ce-b747-94420273c3c3 | -8.48722 | -44.99928 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c26da506-3245-3f65-9a55-843c95126179 | -11.64125 | -45.34821 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08a9c6f4-7051-37f6-8046-d5230ba15207 | -10.35169 | -46.04598 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dc2c4b9-ae6d-369e-b510-1bc8ca9599af | -11.53588 | -43.64389 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57139bb6-634b-3fff-8c07-0586ceeb35ba | -10.43507 | -44.23446 | 2025-09-25 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76cdcd42-20b4-3788-bf87-f96361d889cb | -11.01909 | -45.91462 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3d64c49-334b-362e-ad4c-7e97dda9313b | -12.06884 | -44.84459 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16bac087-1cc7-3b3c-aead-de71efc38fca | -11.04308 | -45.89083 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7eda9594-5edd-3b43-84b7-26b25a8d9674 | -8.16894 | -46.35882 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8cf82dc-0de1-3a88-aa57-13518796b2e0 | -12.84953 | -44.6713 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cb05510-8124-36e1-b665-d57c9f3f576a | -10.28628 | -45.2263 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f98c2787-07a2-30ae-a037-6dee709681a7 | -11.01788 | -44.336 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc16d73f-d80b-3853-82b6-6befbd583245 | -9.76227 | -45.92089 | 2025-09-25 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fc3c71e-c3cd-3f73-9004-5ee9db5b39ee | -9.43459 | -45.58778 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8c2eb38-fbba-3d71-8c48-a06181dd7688 | -12.17399 | -46.57033 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d66fd1a-d73d-38de-afbf-7a8007bca156 | -10.8427 | -44.82489 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fee8beac-5bd2-391e-a8b7-c002408a6698 | -7.99582 | -45.72281 | 2025-09-25 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba8f5ddd-5040-3a89-b397-ac41c57cf60c | -13.84404 | -45.61245 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e80015b-827b-3aea-96c7-826498ca4e3a | -12.54106 | -45.79248 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c019614-be63-3219-8480-d161bda0cb65 | -13.04455 | -47.05244 | 2025-09-25 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d24ec630-9881-340c-a170-3ec5c351b0bd | -10.098 | -46.32152 | 2025-09-25 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 516c98e6-59a5-3ea2-aa17-bfbe6d1e7ff6 | -11.65546 | -44.44516 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73b41ef6-34f9-31fc-9547-5781fd089263 | -10.95629 | -45.66335 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3e51d6-5f7b-3c50-8f3f-d050be60ded3 | -8.69261 | -44.03209 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README23.md)
