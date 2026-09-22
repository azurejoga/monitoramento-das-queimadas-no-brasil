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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a95f72f7-2207-3e1a-b4f2-c7c49f7a89df | -10.4646 | -51.307301 | 2026-09-22 00:57:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ead2a3ba-e39f-33bf-8796-cfea0f774531 | -10.8665 | -56.237301 | 2026-09-22 00:57:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdad608e-54ad-36ac-aff7-c52cdc26aef2 | -5.8056 | -57.741299 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6cbc8d3-c619-346b-9dbf-7183c8107194 | -3.496 | -55.488899 | 2026-09-22 00:57:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 599e49ee-2e4f-3793-9f50-b43a28b4172e | -5.9059 | -55.679501 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a190148-2ef4-353b-b6e1-1cf60a275612 | -5.7571 | -56.526798 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 856fe155-92a2-3015-85c6-c85313885571 | -9.561 | -66.031303 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 645234d6-bee2-39bd-a09b-84896938d6ca | -3.914 | -56.0424 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef9c518f-4462-391c-9572-4b3a51b86860 | -10.9268 | -58.331501 | 2026-09-22 00:57:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d276250a-f1e7-3096-8ef9-6f037f32069e | -6.2491 | -55.435799 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6165cd9d-747a-3848-983a-b3b0efb94ab0 | -3.4704 | -59.585602 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 186d1ef0-662b-34cb-a974-d6577104ffd5 | -6.1368 | -59.883701 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 262608a4-1ec3-3b57-b116-4d35080f4912 | -6.246 | -55.422901 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77d81331-7097-34b4-8d14-92cce73a95b4 | -3.7149 | -60.564098 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68e57b1f-41c8-3adc-8f25-620e045eff56 | -3.5549 | -59.9543 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f99c497-efd9-3b2d-b13d-be8544c79f91 | -3.5763 | -59.059898 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3da277b-3e06-3827-8305-6f006e0bed37 | -6.7324 | -59.423599 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 844df8f8-6ca7-3484-846c-6dd9eef6176a | -2.8594 | -57.7831 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1160b8a1-5799-3964-ac3b-a43363c88966 | -2.4023 | -57.898102 | 2026-09-22 00:57:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b296eb6-9863-3895-9b57-e2ecaf8fd52e | -6.0953 | -57.613998 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7647bc0-4f2b-3bc6-8f1d-b36e55e5031c | -4.2032 | -59.904499 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90e36054-b87e-3ce7-90ff-f7dd7da5f1fb | -3.0724 | -61.2733 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1100274-9ac1-3861-ad55-3d8b52a59a9b | -2.8617 | -57.793301 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 849ba474-cca3-34f4-907b-1cde68e38ba5 | -6.7308 | -55.083401 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e12a66e-d00b-381b-a136-bae172147794 | -10.6046 | -53.978401 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3417cd7-87fa-3680-94e3-e4b2173a41d8 | -7.5763 | -57.684799 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9899e559-0244-31d5-b933-bdb224add385 | -6.9232 | -59.6255 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8c8152d-dc54-3098-891c-b43391a403de | 2.1023 | -60.206699 | 2026-09-22 00:57:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b10f48f7-edff-3c64-8f63-5a622508e8d5 | -3.5416 | -60.572399 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 553c925d-b4b6-3081-b10d-7ff48043f73a | -12.7985 | -54.034599 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff6cff6d-71cd-3b10-9d27-a8fd08a025bd | -4.0912 | -62.083801 | 2026-09-22 00:57:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53ac41e3-7a96-3262-a4b5-0f804b16e86b | -4.2622 | -55.427399 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e2605b-99cf-3d75-aa87-1a6562561c3e | -6.1291 | -59.9398 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 354ab3c0-6484-3e0f-bb37-cd7122874d29 | -3.0777 | -61.160702 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a09175eb-be38-357e-94f2-a600c3b7a0d0 | -3.0711 | -61.176998 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7cf0cf-25a4-37a8-b6a7-7b344fdfb31b | -8.8284 | -50.506001 | 2026-09-22 00:57:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3cb2fd-59db-3157-8b35-2b8df1707b42 | 3.3156 | -61.265701 | 2026-09-22 00:57:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e20d2e29-ac95-3d76-a7a0-f4aaca1b9f4c | 1.7795 | -60.224899 | 2026-09-22 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 90530073-4c59-33ab-a58d-0a5f7fef88bf | -11.7506 | -50.824001 | 2026-09-22 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07f21eb4-0335-3ea0-b54a-5828ba3da9c5 | -6.3107 | -57.741199 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad96709f-7b14-3620-ad48-0b5c33cfcd90 | -6.7177 | -55.0723 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d5fc3a8-89d7-3be2-9155-e152699fed37 | 0.8822 | -60.553001 | 2026-09-22 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9f0054-e410-3d18-b723-f5ff26e61bfa | -3.1889 | -60.426899 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0290432d-21c8-3e74-9357-188be2acead2 | -6.09 | -57.635201 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e124a224-6ecd-335a-a8b9-62f064540337 | -3.0626 | -61.275501 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e019b836-6217-3daf-8b49-53956a8d0501 | -2.8958 | -60.046398 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a976bcf-1b0d-3b2c-9132-49185e3ae5a7 | -4.2557 | -55.443501 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1eb8e8-b7d0-3265-bb1c-e193fe037796 | -6.4352 | -59.9706 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c163137-626f-38d4-821d-010986eef288 | -3.0792 | -61.212399 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b91fac2-1820-3697-bae4-a63f5a0d5e3c | -3.5058 | -55.486698 | 2026-09-22 00:57:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a553b0-3e77-39b8-a821-26be368828a3 | -2.9476 | -57.719799 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8cac2ec-1377-3ecf-9cdd-4433eeb4be30 | -6.7868 | -63.126099 | 2026-09-22 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e67c9942-e6a3-3c45-873a-84b8de6dbbb3 | -7.584 | -57.6735 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab6d0b0-ebfd-3b55-8e22-506ac62566d0 | -6.7895 | -59.134499 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e2c2a50-3bdc-323a-a692-452224546aec | -7.5665 | -57.687099 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa51b3e-7005-3b02-b962-19990f18faa2 | -5.7641 | -56.513401 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3251cde4-11a6-3a4f-ad25-47469a05a3b9 | -3.4201 | -61.306198 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 593a6008-0183-3f0e-8dcc-ed4ab2f7f7f4 | -9.8653 | -55.724499 | 2026-09-22 00:57:00 | METOP-B | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a53c89e5-2838-3019-b4a7-9edda2b0716b | -12.916 | -51.017601 | 2026-09-22 00:57:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f0a7c76-bdf6-3a66-89c8-ce10caf186ca | -6.345 | -57.887699 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8dd9b97-1d91-32b5-a832-426c3eaec448 | -8.6044 | -54.610901 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745e5345-e366-3506-a82a-adf9310293e5 | -6.1185 | -57.756802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc412a7-398f-3fd4-9969-84dfac7eb538 | -8.1022 | -59.8643 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a32ce179-9e8b-358f-af4d-47f9ad2d94ce | -4.0684 | -56.218201 | 2026-09-22 00:57:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e995dc75-49f4-3ede-9ede-3a4b1bdfefaf | -7.0786 | -61.074799 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8152e44b-7f8c-3e85-8538-793cde431e2e | -6.1226 | -59.956799 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d820f699-31b6-3b1f-b42f-a68c5b4372ee | -3.1119 | -60.6768 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d02b3a85-c21f-3ef2-a988-210bac483de0 | -6.1934 | -57.7686 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4012b6-3549-30c1-ae05-3831def40a0e | -3.463 | -59.553501 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 667207e7-601a-3ad1-9bc2-3001413f241a | -6.3353 | -59.939301 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 467a7b37-ae29-315b-ad6f-3f35e06af6fa | -3.6889 | -60.5853 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58645a6d-d626-3b95-8cf6-b98795e7d03d | -11.3126 | -54.0434 | 2026-09-22 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c502e00c-26a9-39b5-988c-240741a42a3e | -6.049 | -57.812099 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e44ae340-3b74-3ed6-bee6-c35e6a6948d7 | -3.0658 | -61.289501 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab3d18a-4762-3161-838c-27cf226415c6 | -3.6759 | -60.6189 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa5c0227-c33d-30e1-a5cc-cb54d49fce8e | -8.9072 | -50.931301 | 2026-09-22 00:57:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46681a60-cf44-3e09-bbe0-9917199b2621 | -7.7113 | -61.229 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1421ce83-6a81-3487-b298-98cbf5b79c48 | -4.2654 | -55.4412 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509a65d6-6aa2-363c-923f-4e373cc407f8 | -6.641 | -59.923599 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a875581f-c52b-359b-a0f6-0fad434ad269 | -5.9794 | -57.690899 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb1442fb-b1cb-3b84-a972-a08d8f2da9cd | -6.4565 | -59.9734 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9616cd9c-f467-31ec-8de5-03dfb0faa080 | -2.8566 | -57.8158 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b96e9d5-6d2c-334b-92c8-62df589d7cbc | -8.6142 | -54.608501 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff716170-0858-3491-bcef-e3b1d663c309 | -3.074 | -61.2803 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87c934cd-5287-3525-bde7-4c0cc1d0ee40 | -8.5883 | -54.6292 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 925a3aa3-599c-3654-97ee-a12888095884 | -3.2802 | -57.866901 | 2026-09-22 00:57:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5e8d1d7-dcc6-3784-9cf0-50cd090c098f | -3.3153 | -59.493599 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec56e6c2-697c-38e7-96b9-85111c0c7af5 | -3.7166 | -60.5714 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ddd6c27d-1add-315d-8b2c-d9f51da3f184 | -5.9297 | -59.969799 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5bccba1a-7ad4-3340-ba9f-bf7583a2f2ff | -6.7243 | -55.056499 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c29a5cd8-3815-3e9c-90e1-baca8cdda97c | -18.7099 | -46.908901 | 2026-09-22 00:57:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b8d3e34f-ab8f-3fcc-9cb2-51d13999cbe7 | -6.2778 | -59.9137 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 345603c2-6d82-3005-95a9-0c0358f6f8e6 | -3.7133 | -60.556801 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db1e66e0-feb4-3d80-a4f6-73719423d474 | -3.2997 | -57.862499 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e27831a-37f9-3a8d-a231-821e2645e790 | -18.7194 | -46.9058 | 2026-09-22 00:57:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee36e2f6-bd76-3f1a-83d1-adae8a034df8 | -3.5782 | -59.068298 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 106f2610-b68c-36ce-85bb-ac0a5aebd29c | -8.4875 | -57.610802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37bf341-7854-3865-8a0b-38fb9bd7afb6 | -6.3059 | -59.945999 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ddc8e6f-d8af-3781-9259-2a3cd5bb7118 | -5.9773 | -57.7701 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70541da3-1fd6-362b-96b3-43cdcd9bc9c9 | -3.1404 | -61.3909 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
