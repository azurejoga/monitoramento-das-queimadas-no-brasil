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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51e813a2-23b1-3470-8a8b-ebabf95b0ce3 | -13.36761 | -43.75893 | 2026-08-01 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d010714-fdf2-30a2-b97a-4557513e9edb | -14.07903 | -46.27277 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bf04f05-05ee-33b3-85a8-ec96650571d2 | -14.079 | -46.22924 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c749aa-0eea-3e1f-85b4-4cd8ea5de246 | -9.87974 | -48.73502 | 2026-08-01 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c6ca1de6-05c5-3c3a-832d-52b96cfce0fe | -8.65021 | -48.26576 | 2026-08-01 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72812190-fff5-35dd-96f3-84d559b122aa | -14.38977 | -48.0813 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b368aa3-cc8f-3bfd-ada2-f1dde4fd6653 | -8.96871 | -45.20314 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83c0aa97-1add-3179-b1e4-e38747e3373c | -9.90759 | -45.74523 | 2026-08-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bd02fb0-4f41-3827-9a98-6c1307d04378 | -9.71766 | -47.3152 | 2026-08-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2829df55-2399-35d5-8666-5a5bd10aeb00 | -11.94016 | -43.43663 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56ad02c9-cbb6-3de2-a605-08e0a9ebcccf | -14.08178 | -46.27686 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3648899e-e4a2-31a5-a78e-cca4e70608b3 | -14.08231 | -46.22978 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51354e1d-cbeb-30bf-b8b2-9683f96146a1 | -15.82242 | -48.17212 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158daf58-8374-394a-ba63-f48663ee35f3 | -15.02444 | -47.05523 | 2026-08-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0fe81f9-bcd1-3029-8772-731fbfd2dd5c | -11.24024 | -54.855 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3948c6bb-d036-3eee-850b-29c9d70cf247 | -15.87979 | -43.59722 | 2026-08-01 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a16524b2-6548-3954-8e2b-848c102445d0 | -14.08288 | -46.26977 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f3fa5dd5-bd42-33b7-9162-60dec88626b2 | -14.08177 | -46.25508 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39fea21f-2ac4-390e-bb3b-8b7354ca8067 | -8.85662 | -45.41957 | 2026-08-01 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 005d2a4b-346f-3b8b-b82e-61514b57438c | -11.23714 | -54.87122 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7400a5d4-e469-3572-9102-bad2c048615b | -14.07352 | -46.2864 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7e75ce35-e1ee-3f70-b583-26a2cbda1ed0 | -8.382 | -48.21474 | 2026-08-01 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15058855-bce3-3505-9c09-03fadf830191 | -14.07076 | -46.26053 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d46deb7-9da5-39f9-8821-01a9c3ed387e | -8.96979 | -45.1962 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d399ca3-5736-3a49-8369-28fdb1030c63 | -14.05988 | -43.82419 | 2026-08-01 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 697feb4d-9c7e-3684-858e-d341914b367a | -10.85268 | -49.11893 | 2026-08-01 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e9df2da-0ba5-3025-a16c-70a6b13ce1b6 | -14.08562 | -46.23032 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e0d1715-5edc-3b0e-9366-f173e06c195f | -14.08233 | -46.27331 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b8320cc1-9b73-30b5-891c-162af745966b | -11.29102 | -47.03855 | 2026-08-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3293583-47c3-30d8-a65b-b4f1b38dcb74 | -11.24816 | -54.87009 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 52d7c1b1-7084-3622-bc44-ebb580c62fbc | -14.40966 | -48.06565 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a29743-bc15-34b7-ba9f-47df681e1cbe | -14.07021 | -46.26407 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1170a15e-0a0f-321e-a98e-cb2d9a3cba48 | -14.07626 | -46.24691 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78c86d5f-b78f-3f6d-b872-643d55444c39 | -14.08618 | -46.24854 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18c42db1-e3cb-3522-a53d-e4d62841c554 | -11.32913 | -44.95169 | 2026-08-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a48539f-ca5b-39d7-b02e-7837d6b54641 | -13.06315 | -52.72209 | 2026-08-01 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e81392bd-1fc6-3005-ae14-3ded04d461a2 | -12.06658 | -45.81303 | 2026-08-01 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce60568b-4a77-311b-b3b7-01b88d38faf8 | -8.97687 | -45.17238 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6c1ced7-b6c8-30fc-84b6-13b551687179 | -11.24725 | -54.84651 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3c4c1e2-43d9-3f13-a9f8-94102541ce45 | -14.34263 | -48.0425 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78d2024b-6f58-3ae5-b826-1f1ff8f05a97 | -11.4403 | -47.23761 | 2026-08-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb17e181-7f8b-3db9-8e1a-49d51390b60d | -13.85854 | -41.33892 | 2026-08-01 04:21:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b879933d-4853-3f30-b84c-7f31fbb21705 | -14.0713 | -46.257 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39f37513-c0b0-3532-bfde-a4e2875216c0 | -14.07187 | -46.27524 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 10d31ac9-b061-3ece-b040-73ccd4261b03 | -8.9967 | -45.17551 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 555b501a-e98d-35fe-a44b-b9cf221865fc | -14.81709 | -48.51581 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb2bbe9-15ad-38a7-8ec5-9fba75ceb144 | -14.41329 | -48.04339 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b3ed799-fd7c-3ada-9286-83172a3494bd | -11.93879 | -43.43767 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa47628-95e3-3255-9a9f-e9ec31234958 | -8.19383 | -55.4395 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 926dc50f-d7d6-38e5-af5f-180acbf6f07c | -11.24145 | -54.84862 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8350e5d4-2f39-3c25-8d70-161f404f69c6 | -10.08165 | -49.12354 | 2026-08-01 04:21:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4befe604-32cd-38d5-a6c0-66548741a091 | -12.3084 | -43.7284 | 2026-08-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3ef297c-ff31-31fd-b403-c0258b29b3e3 | -11.25123 | -54.85395 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 18794448-fbc4-3512-b235-d755dff224bc | -14.15412 | -46.70662 | 2026-08-01 04:21:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1924e73-5201-3f84-a3e4-13af3632297b | -15.82181 | -48.17582 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66952fc0-9d73-356c-bf5f-0e5bfac27ebf | -14.07682 | -46.26515 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0092a841-e8ed-3db3-9977-93b970b116ca | -14.08289 | -46.29156 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0c36879-3c1a-321d-b4c2-347c6a1bf3a8 | -14.07297 | -46.28994 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b88ec86f-23f1-35a7-8c22-c5e9ba5585c3 | -12.60233 | -44.62073 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a06d077b-6db0-3e5a-87b6-2124538dfac6 | -14.34542 | -48.04663 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8c5e478-c934-35ac-bb93-b579960a8c25 | -14.07295 | -46.24638 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f44d32d-fc0a-331f-8390-8173d535cec8 | -14.34101 | -48.03109 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc538c65-4c14-3c69-a654-ea1d3d97dab7 | -14.40993 | -48.04281 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1737e81-6786-3afa-a13b-e273ff712294 | -11.22774 | -54.83574 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbc60a11-f531-3dcd-8765-fd9805dc805c | -14.08454 | -46.28093 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4125d965-e91e-31bd-9aea-241af1759b32 | -11.24482 | -54.85928 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9b6717a8-8ffe-3104-924f-e035ee01a430 | -11.2315 | -54.87091 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 66538aa5-7ac6-34bb-af4e-09215c45a78f | -14.83666 | -48.50313 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a85565-2bf2-30fb-89d4-bcb7b2abe623 | -12.39861 | -46.51609 | 2026-08-01 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5558d6-6cd6-37cf-8daa-48d716b72f7b | -14.07516 | -46.254 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 303512ab-47c6-3209-8229-43774f346188 | -11.24358 | -54.86575 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9e9fbd50-9f34-3815-bdb1-ef96817090c4 | -14.33703 | -48.03428 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 533ba259-6f9b-319f-9627-4ae0614bd527 | -15.44571 | -41.37791 | 2026-08-01 04:21:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1c168fe-cce7-3ffa-bba7-e603f42c8850 | -15.02388 | -47.0588 | 2026-08-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ba8e8c5-6bbc-36ff-9c8e-705bbb05825f | -14.08565 | -46.29563 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d87431e-60c5-3936-89f8-dc5fae5679ec | -11.54636 | -50.13736 | 2026-08-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| adbb171a-84ab-357a-bbdb-40618369d338 | -14.07903 | -46.29456 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20e0f2cb-471e-3b2b-b9d2-4eeb10522fb0 | -11.24664 | -54.84969 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 081c0a13-6c76-3630-9552-a7f12dd426fa | -15.82791 | -48.18069 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf57e76e-1b64-36da-acb0-003ddd7dd476 | -14.86357 | -46.80184 | 2026-08-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b8702b8-c0d5-3d6b-bfc7-b04d3f636962 | -12.241 | -47.18401 | 2026-08-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9c083a9-b46f-3f6b-834c-92020406819b | -11.22707 | -54.83636 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d960c31c-61cb-30d3-b94d-320528f33744 | -11.25062 | -54.85716 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2cd768e1-a652-3948-842b-4fecab6ab086 | -11.2558 | -54.85826 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6a20b7f8-7a0c-3e61-86a3-672a8998f7b5 | -14.07737 | -46.26161 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 247e5ab1-9602-3f3c-aeba-7d033b7dcbe7 | -14.08344 | -46.28801 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddadff7e-163d-31cd-a14f-d51cac335894 | -8.98071 | -45.16943 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 90b0b216-b8c4-31a2-bc41-70f620d5ad37 | -11.22009 | -54.84498 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f01342-2a30-39ea-bc68-b768538a5e65 | -11.23194 | -54.87016 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c312aed3-60a4-3578-99f0-6e0a31e0d5ec | -11.25183 | -54.85075 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a1e7daff-2479-338d-aa6b-51424fe3b9c3 | -8.98402 | -45.16994 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dfe634c-8ba5-3ab3-8e58-86f41c7f7365 | -15.02775 | -47.05577 | 2026-08-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbea9465-08c1-358c-975d-53da221b0c02 | -9.0 | -45.17603 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b338962d-16fb-3641-90e0-25f738e52489 | -14.07902 | -46.251 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38ddbbd2-d870-3475-982f-cfa392c87221 | -14.08675 | -46.28856 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a1bf3f34-e0bc-31d9-bf90-fcf7221a44e4 | -14.07517 | -46.27578 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2accf251-1894-3275-91a7-036f40011c24 | -14.08727 | -46.24146 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6f9a65b-505b-3628-8d37-216a47bbcce3 | -15.5842 | -46.80405 | 2026-08-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee3ea47a-b891-32f4-893a-07885577ccea | -14.0724 | -46.24992 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b3c1ba4-56ba-3e32-bc08-d0ade89b62ba | -14.33763 | -48.03057 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README14.md)
