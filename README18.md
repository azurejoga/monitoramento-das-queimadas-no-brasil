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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c5087c8-a1c4-37b2-b802-b445a516af29 | -11.81222 | -51.89085 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3db1e356-f225-3b14-b1c8-999125969c59 | -13.88964 | -53.82985 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76c62cba-e1df-317e-baeb-e5a8a6ea1d63 | -14.30699 | -51.9936 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f69a5043-0e91-30c6-97e4-7449710f08af | -11.81536 | -51.8287 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb2c48e5-794e-3d0b-a54d-8e02550d9667 | -14.38908 | -52.01487 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f8cbdda-bfaf-3854-95f9-bf4a3fffbee2 | -7.40378 | -59.99641 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b28fcf61-bb16-371f-9334-e35ed2b383ca | -11.48164 | -44.56803 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8c0506b5-fab9-3d79-9f42-10840e0b3ae4 | -15.00848 | -46.60117 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 467c95f3-bde4-3aa8-a1d0-db607da19cde | -13.28614 | -49.63071 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63fd9356-e6bd-3baf-8b72-0a3952e41161 | -9.33948 | -47.52624 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa7efea5-ff34-3bbc-a44a-35d432478269 | -11.80614 | -51.56686 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04ecfc71-55bb-3195-90ce-5cda3d70df8a | -9.76526 | -60.77147 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c532c1d-daab-3f93-a9b6-6b90afa13ff5 | -15.38981 | -52.89485 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d307979a-c437-39e3-b63b-0f8f3c44a4eb | -10.83954 | -50.34727 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e874e785-8492-3022-bf66-be63063becdc | -11.31692 | -45.22249 | 2026-08-12 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14e1cf88-0d2a-3577-a3df-3454aec558ac | -14.48082 | -51.86102 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deaf5e55-9214-3109-815b-bb99f07bb6d4 | -14.27963 | -51.97767 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30d1c090-5799-34f8-a104-345bb22c79e5 | -14.54673 | -50.40304 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebf4e637-52f2-3cac-abf0-99cb50ad8745 | -13.88717 | -53.82225 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19b80d01-bdf7-323a-8016-7980b83d099f | -13.90711 | -53.83315 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e42e3e35-4387-3d7c-88e6-cd59face0ca1 | -14.38575 | -52.01431 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0a606f8b-c61f-30e2-b2ea-d42512b14d1c | -14.30641 | -51.99718 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15e980f9-835f-39b7-be8b-53028739b849 | -12.1823 | -50.15594 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f2f51b5-c7d0-3c65-a320-f722b6822c70 | -11.60629 | -54.66291 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30fe2fe2-5915-3549-8fab-9b2bdd507d32 | -8.51862 | -54.75924 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa64f3a4-8271-32fa-b750-b2a2967c32df | -16.10528 | -49.89007 | 2026-08-12 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c484fa62-7fc6-3e4d-a15d-6364e8e9ea2a | -14.58291 | -46.75056 | 2026-08-12 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b77331d-23cd-3e21-87fc-c5af43e879d6 | -12.10937 | -47.18239 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96e0ae82-62e0-31dc-a43b-85f3da1c60b5 | -11.78509 | -51.84575 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a6aeecb-21eb-3ce6-afeb-a987e07051e2 | -13.56699 | -47.64144 | 2026-08-12 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6706ce2-6a2e-3c6a-b771-f1448eba9eb4 | -13.84019 | -53.80157 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed97f7c-0791-35de-8948-ba1728877314 | -11.46777 | -46.69182 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0095d4a-08ea-3e10-83f4-caab4612cfde | -13.84216 | -53.78983 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51899cad-9944-3467-9893-aa33349e7cc3 | -13.27713 | -49.66718 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28c5db09-a079-3480-805d-4b0077049a9a | -9.37686 | -47.44005 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2be6a1ed-57e5-3925-9c89-960cfff444db | -14.29571 | -51.98407 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7eead54-c8f9-3636-bce5-cd2938acecbd | -13.82977 | -53.82056 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2cef42e-71b0-32a4-90e3-424d929c4289 | -8.95113 | -60.56139 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e80bcc24-d003-37ca-bf85-78bad7856045 | -15.18484 | -52.78083 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43e20776-488d-389c-a327-d955051408d7 | -8.94988 | -60.53635 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| affcd20d-fe10-333e-a27c-8e837e1c58fd | -14.5822 | -46.75571 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7247070-862e-3592-879f-4682da937b5d | -11.4715 | -46.61137 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1668086e-a0d3-329e-8a59-9920a6649eaa | -9.33471 | -47.53374 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96760122-4ec0-3361-8af9-8198d40c18e1 | -11.82425 | -51.83752 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20cfd55f-91ad-3529-9869-24cae25a6490 | -10.09694 | -46.21323 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea154fac-8004-3c0b-bb73-b6fad60bdc17 | -15.05862 | -45.32579 | 2026-08-12 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a345e74a-43e6-3b8f-b514-7f8e716f280a | -9.76603 | -60.7674 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 567f543a-5fc6-3e6f-98f1-f7e913c97503 | -11.60492 | -54.64852 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a408684-8cbb-383b-9d31-ee734f1e2b81 | -11.8276 | -51.83808 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 567e4e62-c0e9-3079-b2f3-f16c5c0769cb | -13.81839 | -53.90932 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26a0c377-f1ef-32d0-bde0-b890cd592e98 | -13.89311 | -53.78653 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc9eac9b-03e3-33e2-a40c-039d675cdd37 | -10.27696 | -48.25571 | 2026-08-12 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bb1b72a-43a9-38bc-b182-9a4bbc7b10ea | -14.35043 | -54.86832 | 2026-08-12 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d66adb26-4f67-31b4-b301-a7dc89f790a7 | -16.10643 | -49.88236 | 2026-08-12 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46e60efe-a6c2-3df7-bb3e-6156c28ae577 | -13.8958 | -53.79383 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b9f9ac-26d1-3317-adbe-2e34588b69e5 | -13.88299 | -53.82573 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10176da5-5612-3e84-91d8-173acecf2722 | -14.58938 | -46.76204 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ddf6bbe-8551-3df1-8860-b0f5a67180a0 | -11.82703 | -51.84167 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ff45a2-a5fb-35f7-b6e8-c74b2e824b96 | -11.47156 | -46.69242 | 2026-08-12 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9db6a67-d7ef-3205-ad20-4d9178ea15ff | -10.22134 | -45.92675 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 03de6e25-2956-3de9-a709-dc67f0b8d542 | -9.47082 | -60.52762 | 2026-08-12 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727b4367-a3f9-31e5-aa3f-0e359fa2da8a | -10.09807 | -46.23285 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 633d1e5f-3798-3769-887f-e12c51a54868 | -13.90565 | -53.82052 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6da79773-a525-36ff-aa5d-d940254c69ac | -11.99641 | -53.45868 | 2026-08-12 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d290947-2563-32d9-a23d-1f0344dfa8ba | -13.83047 | -53.81645 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 744b4ec3-2965-32d4-94f6-6c522283b7dd | -14.34096 | -54.04592 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bcc36b1-2d6c-334c-a907-35376c97cc88 | -10.22523 | -45.92746 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd6a91b3-31b2-334d-984e-dd6b73b593c9 | -9.36057 | -47.45934 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78bf818b-7716-3d88-818c-005a24b2d72d | -8.89494 | -60.57331 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5796c7f8-b00e-39d9-8d1b-526aeea99512 | -11.95611 | -46.3428 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da70b6b4-b90f-323a-9d99-07d69339e276 | -10.43074 | -46.6786 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33099e59-dd3e-3efc-adc2-bfa87ca44bd0 | -12.7298 | -48.44108 | 2026-08-12 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf3839a3-9f2f-3345-8466-ce25b0236b58 | -9.34376 | -47.49807 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7176e4b1-9c66-345c-946f-c2b58051e33b | -14.27946 | -45.28056 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59d00683-161e-3dfc-85fa-91c8c05a9919 | -11.49225 | -54.60751 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c0f09f-3c3c-3d62-b3e9-a7284a174fc8 | -16.10585 | -49.88622 | 2026-08-12 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 39226764-341a-35bc-91e1-2c05ac0df97d | -9.45547 | -51.81281 | 2026-08-12 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c9e857a-9f60-307c-9b8d-616bc33544de | -8.95017 | -60.50322 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb85b3e-2a74-3644-a8a2-74cc92c29dae | -9.33117 | -47.53318 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a6565c8-0c38-3c1f-82ca-14198745e08b | -13.89246 | -53.79046 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a075c840-4fa2-3791-9ba9-0480370aa9bf | -13.89875 | -53.8399 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66f940ab-792a-3239-9378-a8b99e77c150 | -14.47967 | -51.86817 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75f7c4d-4137-35c3-8a42-568b3c25d569 | -11.78612 | -51.86065 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b583d8d7-ce1a-3079-b69c-5a1f83cc66bc | -14.51226 | -49.28556 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b6236d3-6429-398c-8c9b-c317543b6455 | -13.89296 | -53.78933 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fee0b034-375d-30db-97ea-c73e4517a75e | -14.98509 | -46.59285 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d19d651e-825f-3136-a83c-846c894c88e1 | -12.105 | -47.18636 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0020bb5b-d5b3-39a3-a9a4-f800c25b3053 | -13.90779 | -53.82917 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dbff805-ecf8-3327-adb5-2952bf6e8bab | -11.95485 | -46.32357 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbe8c49d-9fca-3ce3-93e4-41907f7ab11b | -9.45208 | -51.81224 | 2026-08-12 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 58002e62-0779-3be3-bf8d-5fa334f76f35 | -11.82529 | -51.85245 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba63796e-f1f8-306a-90d9-93c051c44eb6 | -8.95334 | -60.54958 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f6b7243-e6d6-3dbf-bbee-1e2a922d5793 | -13.88017 | -53.82098 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdf753fc-f8ae-35df-a741-2bc680b96d57 | -13.2743 | -49.66296 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82a0c17a-2c1e-3f57-b15d-32ba9bce07c1 | -11.8231 | -51.8447 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724a5aed-2250-3fda-8acd-6a53db2f9901 | -13.53084 | -46.28327 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f246d684-0ec7-3896-937d-aff1c00937ff | -11.79179 | -51.84688 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19320dec-1663-3b15-9c65-08eaa04f6701 | -14.48528 | -51.85445 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5503b71-f688-33ed-945e-8985bec50a10 | -14.52441 | -49.29919 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c383065e-e983-3530-9346-7635f5931b5a | -9.75874 | -60.77444 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
