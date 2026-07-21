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
| a82f5c43-6d4b-3bc8-8701-9c00e24badd0 | -13.68764 | -48.78211 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2faa585-b6f4-36d5-9e8d-6f7d65e59eaa | -7.65033 | -49.73017 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56b225c2-1aa2-3a92-9ce1-0891e9e5e932 | -12.8694 | -46.87728 | 2026-07-21 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2082006-ee0f-39b3-9346-e3463e503836 | -9.61998 | -47.17831 | 2026-07-21 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af00a710-50b8-3ae0-9138-224fbff3dd22 | -13.30999 | -45.13482 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 35cd40a8-3681-3d1a-8276-781792424f4d | -10.38096 | -49.92727 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 708985e8-e77b-35b7-9dcc-094e46d40759 | -7.9102 | -48.26204 | 2026-07-21 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1596eec2-eaff-30c6-bc0a-9b5d80064c0b | -10.59696 | -46.53665 | 2026-07-21 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f89fc972-4a81-3aed-ab3a-d3949925d754 | -10.55987 | -56.33342 | 2026-07-21 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b425c7f-7d4e-36d6-a5b0-33d756f8c6ca | -7.68932 | -55.36037 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b8b486f-f20e-38bb-9b67-f47eb3cb278c | -11.41386 | -47.5177 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9357310-b173-38cc-a76c-9914f48b75ce | -11.63168 | -58.27937 | 2026-07-21 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a62f79ad-d47d-3f2d-8bdb-38fcef80d9dc | -10.80255 | -50.42755 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bc731ffd-d1b8-3514-bd40-443a085e98c7 | -13.25774 | -42.46526 | 2026-07-21 04:27:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0352f165-edd1-3fa7-a3cd-61738a49c322 | -7.35242 | -49.59945 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| db5604cc-c7a3-3c0d-aa26-7f807e442f4b | -11.59752 | -58.51089 | 2026-07-21 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f785d1d-082f-3bac-b801-06c89aa047db | -7.63898 | -49.75407 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e2a861dd-f2fd-3f20-8fcb-82cf680861ab | -10.38133 | -48.32286 | 2026-07-21 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bed3a9c8-f105-39b4-af92-34705b6cf2ac | -6.54162 | -55.15331 | 2026-07-21 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 944fca95-0fba-3d44-90a1-3ac439fff5e2 | -9.08399 | -50.59916 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597c0256-95ac-3522-8b62-f7601432f3f5 | -7.68876 | -55.36351 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e5a0fa7-c59b-3a35-ac3f-d4745a0a16a1 | -12.66396 | -48.22261 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27f983ce-8799-3ebc-9568-95ede8b86fec | -13.09161 | -48.18416 | 2026-07-21 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6071eb6-cb63-3f72-bb92-ecb1c5b2d23e | -12.52344 | -48.25003 | 2026-07-21 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88353a8d-d987-3b4d-bc49-bbf9375f48a3 | -11.34877 | -47.99657 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c25fd0d5-9613-3ee7-b77d-c44266f6f61d | -11.40835 | -47.50964 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da5b02a0-57f9-3180-afea-1736605ad0d0 | -11.37753 | -47.49035 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f497cfc-e983-3f2b-8a52-e79e77b43f55 | -10.82842 | -50.4276 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 226b3581-90f5-3fdb-8f83-df18878af072 | -10.86215 | -50.42468 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 950b2a19-ae12-3105-950e-2dd8cc39fb24 | -11.59986 | -58.51293 | 2026-07-21 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 789260b7-d49c-3d47-a9d9-46d3d2bf99b8 | -11.39899 | -47.50455 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4abe6d27-9270-31cd-9944-a7de3f01bd14 | -13.69866 | -45.19782 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 826d8bb2-c13f-35a5-8a98-e92b1d253558 | -10.58196 | -50.31129 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae360ac-fa3a-3c6d-b06f-dcff67493c4e | -12.66732 | -48.2014 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0176f685-73cc-3f31-bb8e-047499eb7545 | -10.43719 | -50.20342 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbf908a9-f8d2-32c6-a81a-86c4d5ce4a55 | -11.37479 | -47.50783 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33364ba4-51e2-391e-8cc8-47072f314b1f | -10.56048 | -56.3301 | 2026-07-21 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63d5121a-61f6-3718-9ea5-89de88c3d775 | -7.63176 | -49.7529 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48ec192b-23b3-34f6-9006-cc738dc8ca2e | -10.51729 | -50.2882 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70481bc2-54a1-37e2-b4c1-f1166335c3ad | -10.31151 | -49.64252 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59e40eeb-8c2d-3323-9463-af17f245d371 | -9.08473 | -50.5947 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07353186-45e1-3dd4-a9a9-ab7886f7e896 | -13.68821 | -48.77853 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3b69d8a-9dd2-3730-bedc-8493072fc6f5 | -11.65842 | -49.76126 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8c5400a-c1b3-38cd-bf26-cd72285b29f3 | -7.83451 | -47.11012 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0abff51a-fe62-30da-a63c-710c9cb3e363 | -11.63241 | -58.28079 | 2026-07-21 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 450ae36b-4804-3fdc-90df-c16e01fa399a | -10.63349 | -47.4843 | 2026-07-21 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c928ccec-f4c6-38d1-bb59-a7c2f1b622d7 | -7.83782 | -47.11064 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f1a62f5-9093-3fc7-b1d4-03fec527181e | -13.30705 | -45.13026 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ca5ed0e7-e4fc-3bab-b053-3712a29c6835 | -11.97424 | -47.10806 | 2026-07-21 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9d659b9-e0e6-3e50-ad7c-16c8c4f65b6c | -7.88989 | -46.90887 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9366958-2dab-3878-a916-4b942f8d6925 | -12.4587 | -46.51891 | 2026-07-21 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92e6799c-0779-33ba-b4d8-8f2d3f140353 | -7.68762 | -55.36992 | 2026-07-21 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7944bf7e-2d06-3503-96bc-083da3088755 | -13.31351 | -45.13533 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4325ff47-d092-37d3-af44-dbd19f9b713e | -11.39569 | -47.50402 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdb44a15-8462-3a66-9c16-e567e62730c0 | -13.69806 | -45.20192 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44b083bd-5725-3b7b-bb30-114c23727c0b | -13.3094 | -45.13886 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d030eb9b-8a4e-3c09-bb18-0e661bf92527 | -12.13798 | -48.25581 | 2026-07-21 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 286eb50a-8bdc-3518-a105-d0d523dbd34d | -8.75502 | -49.07986 | 2026-07-21 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 48db04f9-224b-33bd-aecd-1d6c1b233ac6 | -10.85496 | -50.42346 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e6e41d6-3258-3d2b-8dab-39fe5977f8e7 | -6.13182 | -55.80478 | 2026-07-21 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34bd527c-cba3-3b2f-b246-edd6bcdcc6ac | -12.35911 | -47.43336 | 2026-07-21 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91176cdc-9a57-3d4b-8c45-2da5eca31dcb | -13.0883 | -48.18362 | 2026-07-21 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3be48451-c1e4-3b85-9203-37dc666d055d | -10.55586 | -50.2776 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 702ff515-1b6e-3d74-b9d5-bcfea33ad587 | -7.34814 | -49.60302 | 2026-07-21 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 082b823e-4c53-3315-b495-f79dee853825 | -14.62526 | -48.09924 | 2026-07-21 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 294ac170-eaf0-3c5e-9562-80b33b806cdb | -10.80325 | -50.42336 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 57ebb706-4f6c-3240-9fdc-c4f8e2290548 | -11.36983 | -47.49628 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73aa9521-2c34-3dbe-bc70-136d2307f676 | -12.00666 | -50.54855 | 2026-07-21 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aafd54dd-ea48-3df8-af91-cf5ae58525b6 | -10.37741 | -48.3259 | 2026-07-21 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 32f6cbea-57aa-31cd-8cc5-dd80a42ecbf9 | -9.57524 | -49.11252 | 2026-07-21 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0cb8c7a-aff3-30d4-a6a4-a45ef01f9a76 | -12.66727 | -48.22315 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a5f8d2d-1767-32ef-8e81-d69d70ad1606 | -12.45925 | -46.5153 | 2026-07-21 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08a318f4-073d-3701-b909-4e11c96dbc31 | -10.84708 | -50.42644 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e38115b-3b40-33e7-a00d-a73f44d20793 | -6.577 | -55.1657 | 2026-07-21 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1dfa101-b756-36fe-b3dc-fd155c3cef2a | -9.08619 | -50.58578 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1edba241-7abd-3896-b65a-a586eb3548a6 | -11.60071 | -58.50853 | 2026-07-21 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7505012-b2b5-384c-95eb-cbdb9103f9cf | -12.66013 | -48.20386 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec153e90-6c6b-3887-9555-616cebdde808 | -10.38076 | -48.32644 | 2026-07-21 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9a21a20-1356-354c-bf4c-b20285e19b8b | -11.59476 | -58.5075 | 2026-07-21 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ee7454-e316-397f-9426-f212d70b694e | -12.35304 | -47.42879 | 2026-07-21 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7863b1ac-1d2f-31e2-830b-117252af62af | -12.14017 | -48.26342 | 2026-07-21 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a9088f2-caed-36f7-9863-bca7f5787f83 | -12.69273 | -45.32969 | 2026-07-21 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05735682-ceaa-395b-bd7f-2b9c7a74dc38 | -13.3253 | -51.59389 | 2026-07-21 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e31435f6-b00e-3829-b704-fe1e5c5f2bea | -13.56968 | -47.78099 | 2026-07-21 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44ad379e-b0b6-372c-963d-cb8fcfb9c115 | -6.21241 | -57.76002 | 2026-07-21 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82fcecb4-1785-3092-89ca-a3068f185c31 | -13.3141 | -45.13129 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 622e4e36-f504-393f-b237-db797a81f462 | -12.08865 | -53.33958 | 2026-07-21 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d90690b8-a90a-3a54-89ab-6a8d6f3c8263 | -9.70127 | -47.70022 | 2026-07-21 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05a08d1b-ec8e-3d58-b069-d4e179dbe775 | -10.74566 | -44.8364 | 2026-07-21 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f01e688d-43d2-3541-aefd-1071924004d6 | -11.34546 | -47.99603 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02b5d244-faa8-3f47-b4ee-219d5453f993 | -13.30881 | -45.1429 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bbd816aa-fafe-355f-9e39-cb32f0ed255a | -13.55435 | -46.11433 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edb863b1-5074-35b0-ab03-f2f34fcf02eb | -13.31292 | -45.13937 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 01d7e09f-1f17-39af-a980-83dc3452e31d | -11.4078 | -47.51314 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 444737b0-487a-3686-be98-f2365c5e6f9b | -10.55399 | -56.3358 | 2026-07-21 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62652fea-52f0-3b66-9f90-bdc327c0885f | -9.10092 | -59.40687 | 2026-07-21 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 460158af-5bdc-3717-b917-4c12c54464de | -11.38688 | -47.49543 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b020691f-2e5b-34f2-a5c3-7c07584cf4e3 | -13.37076 | -54.31427 | 2026-07-21 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8e52509-7ee2-3bb2-942a-cab9431fe133 | -13.3179 | -51.59257 | 2026-07-21 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03b2535b-25c6-31c8-9559-6fd9a27fed46 | -9.10199 | -59.40134 | 2026-07-21 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README8.md)
