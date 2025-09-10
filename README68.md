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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d3ccfbe-46e7-3aa1-b1e5-58c1960adcd1 | -6.87445 | -47.88654 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6d9cca9-92a2-3b30-bef0-815902b86af3 | -6.5596 | -47.48682 | 2025-09-10 04:42:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1966a18-1897-3259-b5ba-3df48cacf7d5 | -8.38209 | -45.02234 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 895ebb92-7548-3c82-9767-7e6dc328f942 | -11.81744 | -46.7548 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491aa7c6-a18c-3a77-986d-90e0485e0775 | -8.70538 | -48.88311 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef1bb68f-e8cc-3ba3-ae25-a647c82aa188 | -11.11391 | -48.44796 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11839421-6807-389d-a40f-38aa4418203a | -10.63918 | -48.61964 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b96e7bdd-5ec3-32e5-bbce-dc77e721484b | -7.8903 | -46.27074 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 06fe0276-6302-3441-9444-483471a9c91d | -9.06547 | -46.97698 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ab83f61-a26d-3705-a41d-204d0db78e84 | -9.16071 | -45.56865 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1903b985-6021-373b-8941-a13f766624b3 | -9.09326 | -46.96347 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 57d88d38-69e1-38d6-a60a-e351b35aaa7b | -8.49516 | -45.67035 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b51f6955-5450-3eec-bea4-afdbcde55162 | -9.06126 | -46.98059 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9109bbf3-937b-3452-bbf3-1b2362931080 | -8.07799 | -52.35273 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b79079bf-a837-37c4-bdba-10e62416436b | -9.06038 | -45.76665 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6547ec60-5c83-39b7-9a7d-9721b7f5aee2 | -6.58586 | -44.00858 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6677dcb4-6d28-3da2-9b8e-ac1edc09374f | -6.88183 | -47.88388 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5268b34d-81cc-302e-9170-ab078d95ee49 | -9.06732 | -45.71864 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeb438d7-0359-35cd-9603-e2beb3602073 | -9.09563 | -46.97235 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94327bf3-8b7b-3f30-ba5e-98c75df64c8a | -7.62992 | -48.00702 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbaf0884-714e-3d46-b59a-9adbb2da158a | -7.55689 | -44.65738 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f726fa73-31c3-38ac-ba7f-3527db507712 | -9.45064 | -46.73549 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 444e3b05-e2dc-3e7a-9313-2d8632c79e1d | -9.07648 | -45.76425 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc0dba81-9edd-3c8c-bebf-316d557eca28 | -6.84885 | -47.93819 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9a3e644-b1a4-3991-8e3a-e65d9e819e41 | -10.00915 | -51.69127 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7c77a0-b23a-3944-aa31-c47c96b106f0 | -8.69084 | -48.88814 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2aa0bcd-1741-31a5-90c8-f4deddc02bc7 | -6.85168 | -47.91996 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c585bbe2-9521-30fe-8934-2eab19e32b33 | -9.0828 | -47.05892 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e428269f-9458-3e8f-8cf2-10b8d5a6cb0f | -8.04525 | -48.67878 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 560d2724-6760-3b0c-8e5f-5133ee101758 | -10.57678 | -52.04502 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2d626f3-ba6b-3877-b4db-9228cc767f7a | -11.43462 | -49.27911 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e48540-4ab9-3dc7-82eb-dd2672e728f8 | -6.8562 | -47.89088 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 748180a4-34d4-31e3-ab9a-a667a6a31b49 | -9.69463 | -46.8223 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b23dda98-248b-3b7d-810a-832ebea46d74 | -11.10957 | -48.36955 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee275572-5482-30c9-a154-874e7e05e525 | -6.85622 | -47.91318 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f430ab73-4199-356e-8ffa-379c342cf8f0 | -10.02962 | -51.67239 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| de06741c-e9b7-39d9-a214-78978ef7ce3a | -11.11793 | -48.44471 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8de06f5e-0721-3768-9595-03621a9e6ace | -9.06518 | -49.82399 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3365bde7-095d-35c2-a203-c608bf27ce13 | -8.52273 | -45.71008 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45bd0eca-abb4-3833-b9f4-18e794e389aa | -7.35219 | -46.16347 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bca1eeff-d42c-39cd-ba39-cce5239074cf | -10.5736 | -52.02166 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd02297f-f8d5-3e23-8b49-6cc714c5ccbc | -10.52171 | -49.78902 | 2025-09-10 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b395d476-48ed-3c36-b255-7254e918f3c5 | -8.83713 | -48.09383 | 2025-09-10 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 485a7035-6b6d-36c3-bd81-e6334a07c5e4 | -9.0739 | -46.96977 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 814c7c55-1ef5-3015-8ad8-bb65e3b2ae73 | -8.06783 | -50.18742 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3ec284a-8e80-3936-9d11-73f71778df9b | -6.54449 | -49.50924 | 2025-09-10 04:42:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4100b7cf-acf9-3b31-81fe-21842057c7cf | -6.64342 | -51.98853 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09da3b9a-6a6f-3ef5-9742-2af13abea281 | -10.38752 | -48.82748 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b1935b6-bf4c-33c8-93be-7ce0d610d865 | -10.72301 | -48.29272 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac8c1a09-6c34-36aa-8cbe-0489ea4e5e6c | -8.00709 | -45.52435 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 238adb8d-2d81-373b-8baf-7dec4e754fa4 | -9.06177 | -45.75706 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a004d268-bed3-3d68-a061-faedaa0e19a7 | -9.66123 | -46.62449 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3df3658-1431-30f1-ac9f-55dbddaa80e7 | -7.49427 | -48.23346 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4ebc093-e90c-355a-8d80-584e7a242e69 | -9.06463 | -49.82748 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00b33a4-eebf-337b-9870-1f919c527378 | -7.75938 | -50.76243 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b7665c2-e1cf-3c99-8c03-2cd807ae60c4 | -11.34354 | -46.54597 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de8397f8-ba40-3a33-a83f-e5150df4dec5 | -7.53833 | -48.24025 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 039524d6-1216-3e14-83a4-cce05b2a2492 | -9.68324 | -46.89886 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad3f65d2-96e2-3e68-9c1d-46f2e2729878 | -8.06702 | -48.65983 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6324624-15ef-3188-a3a4-e6a68e36ba8f | -11.11419 | -48.36248 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94950c46-e1c8-33ac-a20d-70e997ea24ff | -10.02623 | -51.67181 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 374113cc-606f-3c69-9c45-492816828301 | -6.74503 | -51.96383 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3d5ad32-fc75-32d0-932d-4ac60bbfec55 | -12.02456 | -45.85826 | 2025-09-10 04:42:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f16dab2-5192-3167-be23-7a5d41e5da4b | -9.44274 | -46.71265 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e145348-b4e6-3fe4-9e24-7770295b2dcb | -8.30715 | -44.8203 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27a8798-b3fe-3d35-a8be-de05c3b882af | -11.14944 | -48.3523 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54bc9e04-03cb-37b3-89f5-883a44bc7412 | -8.46463 | -47.2974 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f28181e-ec90-3640-bea1-ff66df45dbc8 | -10.72012 | -48.28838 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20896cd1-0800-3090-a0e1-38ea8b640732 | -9.31338 | -46.73029 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 10341800-db1a-3535-ba2d-224f16065306 | -9.07455 | -50.47105 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d3b8077-2c14-3811-8357-0d9a8e9b8581 | -7.99775 | -46.3257 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0ffc294-a16c-352f-bdff-dd573ed2d78d | -6.87842 | -47.88338 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd9f3f4a-b0b6-3bda-bd45-d2d288c2b86d | -7.55586 | -48.26146 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 528cbdc4-d59e-382b-b11b-55b2aabb1fd7 | -8.41449 | -49.10646 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63b28fee-920e-3b05-a7c1-ef36a28272eb | -9.16055 | -45.57122 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eceb7a21-a1ab-3624-894f-f33888c8d381 | -11.43682 | -43.70565 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66570d65-e36d-3318-b7b0-2521c8ae6303 | -9.06076 | -49.83045 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98b88051-f3f5-3a40-870f-fa5e0392d44c | -11.41416 | -50.43732 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d0f36db-04c2-3328-8cf9-848c2bf05dc8 | -6.41491 | -44.40417 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd92a16d-452f-3b3b-911c-888c29a67a86 | -7.78928 | -46.09692 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90aec71e-16d4-3177-9d76-a7186ee5fd18 | -10.72244 | -48.29652 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f64b27ff-35c8-30d7-b6a7-b0645b5e9dd9 | -6.21152 | -45.6188 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e600ca1-a1e5-3dda-9989-ebfc3fcc25e8 | -6.88189 | -47.90627 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01b5de93-5a8a-343b-9a69-492880e7663e | -9.0703 | -46.96922 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 626aedc3-bf7e-3d2e-9b47-aa0894b03251 | -7.18506 | -44.93277 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d1534800-52d2-37de-b50f-ae65332f440b | -10.15982 | -48.8791 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ad49d8a-90c3-396a-bac3-eab0dd16f9aa | -7.67265 | -50.27136 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e56f4b81-f53a-3d99-9527-013c220b2e2e | -7.3902 | -44.83663 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a86f2228-9d93-3851-8cc5-0b72d87cee94 | -9.08678 | -50.45866 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a9b7ed4-da13-3d72-b573-0b3ade025122 | -11.81368 | -46.75423 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf5fcfce-6d78-3ba5-b6a6-e494c34471e6 | -6.87675 | -47.8943 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e0d2ffc-a420-372f-a9c4-079d396178d6 | -6.20779 | -45.61815 | 2025-09-10 04:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 424d8a0e-e526-3feb-99c7-773412e63529 | -8.05417 | -48.67615 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4289970f-e0f1-3bf5-a7fa-94180030bc62 | -8.69028 | -48.8917 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7b98a60-a02e-3b56-9b8d-f21d62ace802 | -10.02564 | -51.67545 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d2833e-4660-3a7b-b8f6-3e3981c60d01 | -11.66389 | -46.91433 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a40f70ac-6801-38d6-b9bd-9d2565516879 | -6.62818 | -51.83778 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20746ec4-af75-397e-8d42-de6815d9f8f9 | -7.07765 | -45.19969 | 2025-09-10 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa897784-06ef-34bf-bac4-9aa740e2a581 | -11.66574 | -46.90131 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 152a3e7b-64ed-3767-a0ef-6271cd6290df | -9.06907 | -46.97755 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)
