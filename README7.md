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
| a63dc22b-fef3-3382-8d65-84fd0076389e | -9.3758 | -47.617298 | 2025-09-04 00:57:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a4a45b8-6d6c-3479-934b-072a329aecad | -11.538 | -52.215302 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 870fe5ce-4142-31ba-8069-6d27b8b85bfd | -7.5823 | -48.7216 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 60737da1-3e79-3160-80f5-742e264894d7 | -5.813 | -57.743801 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f22315-0733-39c0-bd1a-0b1b127fc2d0 | -10.3335 | -50.371899 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933acc2e-b762-32c7-9d1b-e225897a9316 | -12.0929 | -53.896801 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e05071e8-db39-3013-812a-efc0b9c6ee4a | -12.8205 | -56.957298 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e825779c-fd28-3593-b080-5ff29345d3d1 | -7.6203 | -50.3367 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 183f7a28-c0f0-31c2-9b80-bfef29b94698 | -11.4822 | -52.114799 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7c6b83c-3367-3a8c-ae8c-2471f4400fed | -6.7738 | -52.794201 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9e21718-518c-3257-83b5-a4ee03405def | -22.138901 | -55.989101 | 2025-09-04 00:57:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b2e1b3f-963f-37ab-bae6-a76f98f246af | -15.8961 | -55.968201 | 2025-09-04 00:57:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d716de57-1fb1-3633-a321-997283eb508c | -6.677 | -63.132198 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed5d6249-ced6-3d9a-a280-4d45970e5954 | -16.424101 | -51.899799 | 2025-09-04 00:57:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa3140ec-421b-3f4f-9e03-2b1430c12786 | -3.3432 | -59.571999 | 2025-09-04 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92fe70a6-5425-3f7f-b8ce-2bace6bbcc55 | -13.6306 | -46.922798 | 2025-09-04 00:57:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09554501-2335-3302-b20f-3225bcd1bbe9 | -14.9479 | -50.084301 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24cbefc1-7f4f-3017-93d7-cd922c696e41 | -15.2025 | -52.779598 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1544b6a-582a-3000-8fc0-be282671c1aa | -22.0716 | -56.487999 | 2025-09-04 00:57:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e28081a7-baa9-3f76-9664-1b6f334195a1 | -14.9105 | -50.059502 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad2d167-7813-3ab2-8f16-750074dc262f | -16.367001 | -49.527802 | 2025-09-04 00:57:00 | METOP-B | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9935c6e-7678-3e23-b809-f0c3b66ab8b0 | -5.1869 | -55.9664 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd3f5e9-c246-378a-9765-d9eb8fdbb4f4 | -11.7833 | -51.540901 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46a7d0dc-7a3d-3471-8df9-ad8ce8951c0c | -6.6734 | -63.1157 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5de2f4e-f937-39e3-bd68-1d3cc3f50c5c | -12.8322 | -57.008701 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53d5f6fd-55dc-3219-a388-89e5f3c6e8b0 | -11.5635 | -54.5327 | 2025-09-04 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10869988-1b89-3069-b0b8-d34778294735 | -11.4922 | -52.155499 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4f8ac4-746e-34b5-bd1d-d58a5fe4b23e | -13.0138 | -57.127499 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24d53eba-49e3-31dd-bbee-727a7d8c16e4 | -15.5099 | -52.894199 | 2025-09-04 00:57:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1089f93-5d83-3dcf-b933-3e45f85f5762 | -12.8269 | -56.940201 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6850b858-ced1-3ec3-817f-ec1a0ab2baa3 | -10.4052 | -50.451599 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 476c2930-7fc2-3d96-a809-e216b6e74b71 | -16.7178 | -51.3354 | 2025-09-04 00:57:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 132d13b3-63f9-349b-a55e-0d3361c566d3 | -5.7791 | -57.7757 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d46094-584e-3027-8b10-a7460199f983 | -11.7573 | -51.437199 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b62a1bb-2f2c-3c52-aabe-0cdb53ffcf15 | -12.5528 | -57.004799 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f17a4a2c-1150-349d-8c5b-5d30d0af0c7e | -5.8246 | -57.749298 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e2d8c19-ec4d-3ef6-ae16-584ad9ca8fec | -12.8107 | -56.959599 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7615281d-b0d2-3f5c-9b7e-4562556038c9 | -4.9067 | -56.268501 | 2025-09-04 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d14acdfb-10a9-314a-ac73-5e2979874cfa | -6.6886 | -63.138401 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8da5a914-d548-3df1-823e-5a340e94b14f | -11.5612 | -54.523102 | 2025-09-04 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf9e14df-45a8-333d-b84a-ce2634ca5f21 | -14.4839 | -54.561798 | 2025-09-04 00:57:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22d5d35e-7594-32e4-a6b1-e224a0b50d77 | -12.8885 | -54.805901 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37a56dcd-3a80-3037-b0ed-febb7aa82a24 | -15.5125 | -52.9048 | 2025-09-04 00:57:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21e0aea2-f941-37d0-934c-775cb34a983c | -11.5538 | -54.535099 | 2025-09-04 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3122ef1f-9e1f-30ae-b7d0-6c14874cb124 | -16.721001 | -51.348099 | 2025-09-04 00:57:00 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2b757b9d-583a-34b6-ac7c-4d1094fc40da | -12.8056 | -56.9375 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12496750-a939-3dae-8587-6d38a24cf75f | -13.6382 | -46.9506 | 2025-09-04 00:57:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4674ebc9-1bfd-378a-b2f6-35f267c0a43f | -12.8864 | -54.796902 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3759c1a-fb40-3df9-98e6-d85f96299e28 | -5.7693 | -57.777901 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 384cc0cd-3641-3fb1-b40c-7a5fc2fd8af1 | -11.5906 | -57.3535 | 2025-09-04 00:57:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 170c2cee-e60e-34bc-8a98-583070b51109 | -11.1154 | -55.0378 | 2025-09-04 00:57:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b11d69f-25c4-310f-a1f4-082ea91c7522 | -12.8338 | -57.015999 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 962d01cf-8193-3697-8ba7-c1c745a630cd | -22.628799 | -50.573601 | 2025-09-04 00:57:00 | METOP-B | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 00afe7aa-06ee-306c-b71a-c2d9d96073a2 | -14.9286 | -50.089699 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00312a23-5edf-369e-9e5f-af7815804346 | -12.7975 | -56.947102 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41c4350b-47a9-3b26-8675-7dfc08fc8bab | -11.5478 | -52.212898 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46559cb4-31e2-3b68-b20f-49373ab458c6 | -12.5235 | -57.0117 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be5ed49b-ddcf-3091-a293-f3934c618bf1 | -8.2632 | -48.3414 | 2025-09-04 00:57:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cfd9bc2-955f-3416-a37f-bc7f1f3f759b | -6.0063 | -57.732101 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eaa191f-8671-38c2-b69d-d82119c2af96 | -14.9437 | -50.067902 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 15cb9bb6-04f6-3157-9074-6f1d934288b6 | -10.3481 | -50.348301 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef5976fa-8c6c-3d5f-9ea6-1848d886bfc6 | -10.5216 | -55.408901 | 2025-09-04 00:57:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7295a6d4-6a54-3471-a011-174ea5eabbc4 | -11.5511 | -52.2262 | 2025-09-04 00:57:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50d89362-e48c-3e9e-afa8-f3cf64b12a17 | -6.6672 | -63.134399 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9335ea95-abf5-32bc-b610-59886323163e | -9.408 | -57.820801 | 2025-09-04 00:57:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a380cd-637f-3f45-b70d-930e3505316a | -11.7662 | -51.513901 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f2f07634-2317-33ed-bc8f-eedf26b0b28d | -12.8821 | -54.778999 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 221cd667-124a-3d5a-a363-adac35b9536e | -12.8009 | -56.961899 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c36c3c10-207a-3228-a874-466d0ebdba1d | -16.223101 | -52.975101 | 2025-09-04 00:57:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c18fdd61-42ab-3f56-b1b9-59959cad8c44 | -12.8286 | -56.947601 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f754c12-f760-3dc0-a927-6e4d68439793 | -11.7736 | -51.5434 | 2025-09-04 00:57:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef3e738d-39f3-39d8-aeb1-c2bf64b9dfb4 | -5.8291 | -57.7239 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0cc83fb-3973-3cc8-b9b1-ecccf021d578 | -14.9159 | -50.040501 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb02195-6ea6-335b-9ec7-a9d5e2d83d06 | -6.8612 | -62.9888 | 2025-09-04 00:57:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90c4fd30-ebd3-371f-9483-33d19aa65296 | -10.3782 | -53.637501 | 2025-09-04 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3371e81-6d0a-34ee-a899-71c27978861c | -6.6788 | -63.140499 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3773f21a-d0fa-32ff-b4ff-43280f0c944f | -14.9383 | -50.087002 | 2025-09-04 00:57:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2b84c581-e290-35fc-83f0-7e74e059cb2c | -10.8671 | -49.758099 | 2025-09-04 00:57:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aea113e9-bb31-3aa7-87c1-d2f1ecda2277 | -7.6099 | -50.295101 | 2025-09-04 00:57:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d591bf14-bc6c-3a17-9498-cb77431cbb93 | -12.3903 | -53.844501 | 2025-09-04 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32955a0a-c1e5-3c91-b4e4-a55470956125 | -12.3983 | -48.0872 | 2025-09-04 00:57:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35102f41-55a9-33d0-ac30-950772f45a96 | -22.5583 | -43.7145 | 2025-09-04 00:57:00 | METOP-B | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbfea367-8742-3dda-913f-106379da66dd | -6.6752 | -63.123901 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 587ababa-06e6-35ea-ad31-9e2f14c84bcb | -12.8842 | -54.787998 | 2025-09-04 00:57:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a15e335-8338-3c27-84c3-47c090549719 | -15.2041 | -52.744301 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd2899a-78f5-3982-86e5-98533e26f9c4 | -5.8032 | -57.745998 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a6bb64-7620-314c-be51-1581c28582cc | -9.1775 | -56.904701 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62b5b92f-dda6-31aa-8a77-100634ad6869 | -6.7002 | -63.1446 | 2025-09-04 00:57:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e612f54c-1f4c-3720-aee8-b5d46e3176c0 | -22.6259 | -50.561901 | 2025-09-04 00:57:00 | METOP-B | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 20a31abc-9584-3040-a220-15206003a871 | -5.8211 | -57.733898 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feafc3d1-c992-3ba3-a0f5-13252ef69192 | -18.0361 | -51.798599 | 2025-09-04 00:57:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4558ece-e453-30b3-87c9-e2b920d2d24f | -2.8657 | -49.362598 | 2025-09-04 00:57:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e4ad55f-d8e4-3107-b348-8bcefe78bcb4 | -15.2095 | -52.766102 | 2025-09-04 00:57:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8efc7c93-8e84-3d34-80ff-96193e49e95a | -14.4659 | -48.0606 | 2025-09-04 00:57:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c013e19-90be-3a44-b25a-00463c54ac17 | -3.3448 | -59.578999 | 2025-09-04 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb59d356-799b-3ea8-bb55-ffe1fda4bf2e | -12.8073 | -56.944801 | 2025-09-04 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 985c9f07-682b-3110-84a2-b84a1c760e20 | -10.3431 | -50.3694 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5911f6b-d595-3026-8c0f-efcd6f08b1e8 | -5.7711 | -57.785599 | 2025-09-04 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e100374-3ded-37cd-9bd8-8bcefb7da74e | -20.0056 | -50.028702 | 2025-09-04 00:57:00 | METOP-B | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 78c8fb7a-30a0-3463-abf3-e17ce02aed91 | -10.3525 | -50.406502 | 2025-09-04 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
