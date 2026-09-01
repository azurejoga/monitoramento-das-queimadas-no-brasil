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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a6e5119-5f38-3afc-84ed-7c447ccd5b45 | -5.95516 | -57.68955 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca2219f2-eeb9-3871-86cc-35fe9417d1d6 | -11.9269 | -45.09729 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6307fef-74f2-3d39-93e2-59b95fae5b79 | -11.20795 | -46.07592 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8181973-b3a8-3dcf-8e3f-6fda0f04bcd9 | -7.35062 | -55.19973 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74ad4038-4168-395b-96cc-5430990bff5a | -11.47944 | -45.08384 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09ab4e87-45c8-38dd-9778-4a3755aab1d4 | -6.94619 | -55.63384 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b106ce-f293-31cf-82a0-7bd2b0fa8277 | -6.70652 | -55.4077 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc4fe888-8b56-3bff-b510-a9b02f48744b | -8.59174 | -54.72514 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b0c535b-cf76-3437-9bfb-f4819d726dfc | -11.2981 | -50.59033 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a39fdc8e-50fe-3835-bce5-2c1ea8f7e9ad | -6.8225 | -58.87441 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce74aa0a-9e67-39a1-9e6c-7785f662c1b9 | -10.36147 | -50.01012 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 741444e6-fa6f-37db-bbe6-bc8fbf582c49 | -11.24728 | -54.00449 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65fe8e1b-a6f9-3011-b608-74772ca00d93 | -6.26019 | -55.42772 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba1c6d85-2440-3670-84ea-6754eda47873 | -8.49378 | -44.75027 | 2026-09-01 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85632a18-db66-3daf-a632-c835637cedf3 | -9.67963 | -50.8493 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdd00561-b9cb-359f-aa2b-fe5b9fa568aa | -5.60755 | -43.99884 | 2026-09-01 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 070d42d0-8a24-305c-923a-3cf822162984 | -9.15253 | -59.53912 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e972baa2-7e00-3553-aa6b-3511149ed703 | -6.60213 | -58.59386 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8f2ed5c-a93a-3f20-afac-2b0105bb425e | -10.20836 | -50.31852 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 130122c8-b7c8-3ec2-8ff3-8eeafdb28a6a | -5.48324 | -57.15182 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4a0e028-2430-3a3b-aa6c-0cb8ba6504f8 | -5.347 | -45.16105 | 2026-09-01 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e8bdcc34-d575-3461-8b36-42a66dff17cf | -10.82981 | -50.71543 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da84eedb-65f6-3164-8f12-de1ef4336879 | -8.79826 | -62.51311 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86ab7cb0-c73b-3bc0-a852-c1785c6f71c0 | -10.67656 | -46.2748 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f951847a-e284-3980-8f8f-7d7aa60c620f | -11.66348 | -47.61282 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a8ae1df-b3ec-312e-983b-61d7f12f5352 | -7.02679 | -55.64356 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5570a760-91cd-3f89-8767-cbb207d869a7 | -9.45388 | -45.62177 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8006b006-ca19-3309-ac58-173e38cf5900 | -5.25538 | -55.89182 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75b7732b-b4a9-3cdf-9d93-d2d6735a8205 | -4.85533 | -55.82757 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1f38470-bf18-3fa2-bccc-06a658bec76f | -8.59183 | -54.77147 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43d30f96-860e-30b9-852a-81abbd16c977 | -10.34821 | -50.00803 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5125ca72-dd50-3437-9967-eb804db9b028 | -6.80329 | -59.45601 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4281ee14-8a74-3205-bb10-b36878856b7f | -10.83752 | -50.70949 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26fe1398-9d5c-3ad2-8cfb-771085da439b | -8.93464 | -62.35995 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9979e141-fc31-3b22-9646-52a293bb06d0 | -11.65987 | -47.61227 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 464d4019-89cc-3ffb-a127-3c2ea82b103f | -5.73669 | -43.27764 | 2026-09-01 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a3404ba-8f39-3794-a8ca-2fa0f93c0279 | -8.49074 | -44.74234 | 2026-09-01 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c0536d3c-c07f-3887-971d-f8baebfd0857 | -6.98384 | -59.59417 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36146b6d-103f-3eb2-8096-14bd1a12bcc9 | -10.69139 | -46.25259 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb309d45-a381-394a-9840-962aa203513c | -10.40589 | -48.22585 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32541c78-2762-3011-b630-e753d5db000e | -11.10709 | -51.54407 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d4162ee3-0fe5-3134-afe8-f0858c884fe0 | -7.30718 | -60.56628 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5467cb0-e6ce-3106-96c8-e45a62fe1aa6 | -11.90738 | -45.07907 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdf1cb0b-c0b3-3995-bbd8-22bbfc936c79 | -11.93476 | -45.1027 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae750b10-80d5-3d73-8bd1-4189cd61c7d5 | -10.40867 | -45.08001 | 2026-09-01 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c48dc790-2d80-3509-a82b-eece9be0b794 | -10.34929 | -50.00102 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| df6cbb47-7eb5-3be1-82a0-cac6b641409a | -11.48201 | -45.09606 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 962f774f-3cf2-3627-ab76-da553f9ad889 | -6.59631 | -58.59628 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f66bea8-f27e-3141-8810-31515dcd5c58 | -8.42069 | -45.00042 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67f842cc-351f-3ea1-a048-d218b3b4c84b | -8.41718 | -44.99617 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d864bf6a-c0c7-3260-b5a0-751092a109ec | -8.27154 | -54.92533 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 6c084de8-08d8-30a3-9fac-e1c3e7257e7e | -5.95958 | -53.60798 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deb2039c-5c10-39cf-b9ef-55699dfe5095 | -11.51988 | -46.92716 | 2026-09-01 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c23bf3b5-6d59-32de-9518-d6472504e7ed | -11.65689 | -47.60751 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e61e0206-55eb-3136-9d46-1233f59c9e18 | -7.02397 | -59.65137 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beeced86-fd5a-38a1-8bd0-62f0e9007db9 | -4.79722 | -55.97943 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b750efb7-301b-3711-b1f0-682bff3cdedc | -5.75618 | -44.12589 | 2026-09-01 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8455d60-54f9-3a3d-b85e-ed88e38608a2 | -4.34569 | -55.44336 | 2026-09-01 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7daa0455-98bb-3a73-94da-a1515fc44d46 | -10.8254 | -50.7219 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f5000ab-f47c-3525-a0ce-a0d16d99b951 | -6.35499 | -55.86221 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 926c5c37-fe3f-3b8f-8ea8-f092610a34d4 | -5.58357 | -60.23764 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 345507f7-f1ce-3936-aeae-51ce521db698 | -9.99913 | -46.39478 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ce9f14-35e6-3159-950a-8bc2f4431461 | -11.29864 | -50.58683 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 77b6e3de-134d-35bc-b4b6-af83e8065951 | -11.26279 | -50.57752 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbc52fc4-b746-389c-a2c2-5917780168b4 | -11.11099 | -51.54106 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1091aa42-763a-3ae5-a6c3-c0ed99359751 | -11.26283 | -50.59906 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 052764be-9b02-3ba1-9c3d-b3ce42425ff1 | -6.13159 | -56.38825 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 064c89f1-3494-38f5-b2eb-470cc311b2ad | -11.31554 | -45.18171 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 67c6f1e5-0ec4-366d-aff3-70a898beb9a6 | -7.63248 | -55.2863 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31c2500b-2a88-30b3-add4-55323aecfb58 | -9.98287 | -53.93002 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aac9fcb-8bf6-34ab-a0ff-ed91231388cb | -8.8564 | -48.49426 | 2026-09-01 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f94ec4d-c5ea-39d3-9b76-5935f2096fd0 | -7.04931 | -45.39803 | 2026-09-01 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a773fe73-41c8-3515-a21a-e041ab37daf0 | -7.53065 | -61.38047 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0be99f08-0fe6-346a-8c4c-186d2a4a4f1e | -7.0261 | -55.64756 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78c15576-ba3e-3420-96ec-1512c12f9cc0 | -6.34576 | -44.09698 | 2026-09-01 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b985efc-c84e-3547-b090-1c72bf205c71 | -7.88756 | -47.0772 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24f344b2-9c45-3cc2-8cf6-a36ecd655fca | -7.62369 | -55.29669 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55a4b883-6572-31d3-902b-d839215cb9ac | -4.96426 | -55.85229 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0013ae37-209f-3355-8e92-23c31ec1cfcc | -11.67251 | -47.60146 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81838fb7-75e1-3b48-9d0c-d36a41afe997 | -11.06595 | -51.52602 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78f92947-0752-3eee-9ccc-02b7cdecf15c | -7.3013 | -60.56517 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9c4edbb-d6ff-3986-a93f-525ee823f632 | -6.745 | -55.66863 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6412845c-ea59-3d03-b8e9-c814e415437a | -8.79973 | -46.36656 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45c5a200-bea5-3a13-96d1-df6aadf453f0 | -11.25893 | -50.58049 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db87a892-40ae-3c36-b459-97a74f1286e1 | -5.9447 | -57.69067 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d0038ce-e04e-396d-8693-4fca8e3c1eaa | -6.59934 | -58.60995 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b673a5c4-39f0-3960-b83a-c4e502b37172 | -6.65506 | -59.42862 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed0a704a-50b2-3260-8b89-b28cd497e51e | -3.26399 | -58.23837 | 2026-09-01 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c38998e-3601-3823-9287-65b789ab7d91 | -6.38227 | -55.21896 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba41f5b4-0940-3c68-a835-2207e3ab7775 | -10.23566 | -54.34798 | 2026-09-01 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f85ea9-8b8f-338d-9569-59cbd8143a3d | -7.92441 | -44.231 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bacf8e2-3707-31c3-9c82-ff3bb5fc3e42 | -10.84238 | -50.63499 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d38b5ce0-5c3a-323e-b31f-5f16b9705d8e | -6.95335 | -55.64327 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7af6cd31-5040-32a7-b80b-e502f63d34f8 | -5.8805 | -52.05639 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae52e800-8581-3bc8-a04c-56863ec6e241 | -6.1224 | -57.67271 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bede1837-b408-3ee1-8533-54d8a9e1c2f9 | -9.92708 | -60.49314 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3be4b63-e4ec-30ae-b67c-618753e5b6e6 | -5.25084 | -55.9018 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 457e8e8a-6e02-38ce-8a7a-77a8647e03a8 | -6.6769 | -52.87623 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d03a2d11-bf62-301f-9a39-9860b476f29f | -11.30199 | -50.60889 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c3b126a-e709-3e6c-83c9-c754435861a8 | -7.94941 | -52.45773 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
