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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 112819c9-5608-39ff-aa8d-c5fb067e8cfa | -10.98953 | -45.39738 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 378482a7-9325-33da-a5ed-f4e95f752f4f | -7.57782 | -45.64693 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 872bba83-54c7-3656-bffa-4e7fb8b91dcc | -8.49847 | -54.62566 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258c0f5b-7806-3daa-93c8-449c40f16e30 | -13.36759 | -43.89132 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c5d1536-6e1f-3ac9-9165-4d6bb0c5d2d3 | -11.99909 | -43.47776 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7cb7f0ec-3767-3c8c-8b01-ad139c068f18 | -7.29005 | -45.41714 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7a5b272-7b07-3d9c-88ad-4d334ec96653 | -8.94955 | -45.18633 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f141741-4476-3442-a62d-23031034826f | -12.22993 | -57.10303 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29eac8ef-a942-38f9-8373-29bb2b00ad77 | -7.18255 | -52.61369 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e8fcac1-98f6-37b6-aa96-d9eed553b1c5 | -9.83616 | -44.78348 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00c36863-9ddc-3101-8817-79a76c6510f6 | -6.85693 | -48.7772 | 2026-10-09 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39afaaec-02ed-382e-a156-b001dcb5d8f8 | -11.58789 | -43.65324 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 871416c0-4e7b-36fa-8b1b-7ad1eefbe896 | -7.18829 | -52.63136 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9359cc80-e387-3c01-b446-51f8fcc34a8e | -6.48938 | -55.29878 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e006626d-eb65-3a0e-9310-6be5cb373396 | -8.90272 | -44.93788 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8a85870-1ca8-3e2f-af08-e34d0723833e | -11.33577 | -46.6601 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eda2881c-7b79-3bb5-808e-985705089d40 | -6.48831 | -55.30505 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a2f6925-d047-3353-a144-e9a5254a17b8 | -13.12929 | -46.3251 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb389765-1e7b-3849-a3d0-0a1f54cd5eb6 | -12.22056 | -57.10054 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 0fa7f0e7-d933-3281-b55c-1c57cf3af896 | -13.38705 | -46.68812 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d7c622c-2cc8-3178-9dfe-bc2a3b0bd56a | -12.21935 | -57.1011 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 64e33ae5-71f0-3d6f-b39b-3a365d65e4b2 | -13.40878 | -39.79756 | 2026-10-09 04:27:00 | NOAA-21 | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 85d50042-84c3-38da-89d5-ab59fe80feff | -8.03804 | -49.40056 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d251ce83-68a1-37da-ae9d-3700d993f8be | -12.2082 | -57.1301 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43f0e367-fb21-3a0a-a52b-384680143471 | -8.13742 | -49.43678 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32635b81-5b99-34a1-a885-8c807ee69bbe | -12.21865 | -57.1107 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2f1d9e3e-5b3c-32bb-a388-d20accb9b0d4 | -8.73812 | -45.14661 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d0aef17-3a2f-3726-a931-e7c4b6c3ee19 | -10.78509 | -49.71753 | 2026-10-09 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 255f9b2b-af7f-31b7-a9c0-8df6eeb46a48 | -9.87354 | -50.49637 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 103f7fb6-948b-3464-a1f4-23d5da6366c6 | -9.29591 | -47.46335 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db86e20f-4895-302f-a6a7-2cd05e739d35 | -12.2134 | -57.10354 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28845a41-5520-38f9-bb4c-8653ffffb287 | -11.59298 | -43.64449 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aef99407-f4a2-30e3-b2db-ff80bedf6c11 | -7.50338 | -54.99897 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50fd82c-c7c0-3ba9-8305-10dd243f101d | -9.02824 | -46.86941 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5670623d-e877-3579-ac76-7061aec07e70 | -12.22306 | -57.0872 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| dd30985c-310c-3e5e-9188-a2fa41b1a024 | -12.23649 | -57.09746 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c6b881f7-c892-33d0-aea4-29734eecc160 | -10.01896 | -48.54841 | 2026-10-09 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32504fc7-4fbe-3fda-8343-3996d6ed22a7 | -7.56243 | -46.68925 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 122ff9c1-a4e7-307a-9eb2-ba011c4869f8 | -6.38064 | -56.23146 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd208455-dc47-3a8a-a960-7f1051f3dc56 | -8.04153 | -49.40112 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f026b62c-91f7-3f2f-99ae-5519d60fed29 | -6.99084 | -59.10458 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71144dca-a7a1-30b9-819b-eec684639d31 | -9.34865 | -46.58171 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 538b44ba-72f4-3aec-8edd-62c45bf077e7 | -8.16425 | -46.80268 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b84f83e-bb67-3695-9f2d-8dbc5dee0c96 | -11.82854 | -43.59315 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 70d760e8-9548-3711-aaa7-2a897ebc66e5 | -12.22341 | -57.13652 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 153d7598-b9de-3418-9a7a-983380bf609d | -13.15523 | -54.34202 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 466e5a9e-8dcb-30a0-9ea0-3f880f948dc1 | -11.91125 | -46.56358 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c90003b5-5ece-3cea-9cdf-fb492996fc39 | -14.60594 | -46.57597 | 2026-10-09 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| afaa54df-8504-391c-a28c-233d1c0468d1 | -5.99172 | -55.36732 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6373b2b7-bbd3-3cf3-9b2d-7dbedc6f06c4 | -6.456 | -55.49343 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb6bace-bc0b-3f70-9339-cbdd092bcc5d | -14.44349 | -43.93185 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba037335-4552-3252-9b88-3e591a57beac | -5.98756 | -55.36013 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45fe9de7-7ce8-3166-8320-41fea9ccceec | -6.00175 | -53.49498 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5404445-ba48-3c08-9041-16ab270069cc | -9.20959 | -57.72312 | 2026-10-09 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccc7612b-d659-305c-bc60-d974091c5de6 | -6.92808 | -59.26637 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63e532f1-e562-3a53-9ed2-2678d0cfc090 | -6.99187 | -59.10332 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2718e1a1-3cbe-3421-8e76-b6cce221360e | -12.20371 | -57.13188 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05e1253c-67b2-37e2-b8c2-02c79f11bbcc | -7.89978 | -54.71844 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b433a7f9-3c37-3b44-879b-dd79fc33b52d | -7.17829 | -52.6129 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 711fbdb9-3515-35e8-8bf3-bbd5025692b9 | -9.09894 | -59.38613 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cebcc1f-88b4-3efd-a3dd-75844bd357c6 | -6.48992 | -55.29564 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a822ec5-73f8-3890-a749-ce746339afaa | -6.25733 | -52.86085 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c43d411-b4b3-3c50-8a2b-aa4026879264 | -12.37195 | -39.47762 | 2026-10-09 04:27:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b3a8926-3489-381a-8b2c-c04dedf9135a | -6.13103 | -55.68219 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d2fd291-50f2-38ce-a949-6c5eea254454 | -13.15749 | -54.32939 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2525df3-4501-3dfc-aba2-01432693d598 | -13.17418 | -54.31078 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92e68425-53bf-361a-926a-6446698ba376 | -11.46351 | -43.38265 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d24d27b1-ab24-3a63-8a65-6ea00f283d62 | -11.61044 | -43.71664 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6edb558a-1f1c-33d5-9e66-047bfaae1c5d | -10.92505 | -45.3842 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a8f1aed-9b4e-347e-8150-9c690b190207 | -7.29156 | -46.15762 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7020e69-5d67-30fb-a2f9-b76f6f6f78ee | -12.17767 | -57.09582 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfb79632-430d-31ff-87ec-fdd74a1533e7 | -11.7485 | -61.06568 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fa2cca82-95c5-3284-9138-1b63d17bebe7 | -12.18476 | -44.64842 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d05490f6-20b2-3ca3-a589-cef40e29967d | -6.4913 | -55.29544 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17e24a5b-72a8-30d1-89a1-a4ffc44b1934 | -6.73073 | -48.12016 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac63f0b9-fd82-3702-8eb0-416eb6ff7fd6 | -11.77769 | -45.56507 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 001fb284-ce2d-37b6-bc70-4962086121b6 | -7.79402 | -44.57318 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46e92aef-12a6-338a-b6d2-9b2d37840ad5 | -6.47578 | -55.47343 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e266e0e-0089-3edb-8862-5bafa32fa688 | -12.20162 | -57.13565 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31da4574-92c0-36c1-beb5-a8d315f8d1f8 | -7.18898 | -52.62731 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4f6a007d-0525-36c6-a570-77bb3ba3f8f6 | -12.09985 | -57.15748 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c50642-d2f5-3b08-914d-3ee9d3c90987 | -12.22001 | -57.09774 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| afb54e01-2244-339c-994e-d3ac0c9218fa | -6.49716 | -55.96149 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b762532-02cd-3af7-8f88-5fc0ccf1271a | -11.83923 | -43.59953 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5768531b-c466-3a78-b046-19df05a51519 | -12.2087 | -57.10541 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ebadc15-f784-31a6-8927-e42c8d81e426 | -14.44868 | -43.92253 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff93f9f9-7814-3ede-9068-f66aaeea0e23 | -11.63169 | -54.53943 | 2026-10-09 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2675ed82-eac4-3332-a420-909e6abdaf3b | -6.45331 | -55.04834 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 128c3884-7fb9-33f8-980d-accd7835229a | -12.21085 | -57.12308 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c64dc21a-cc9d-322e-8c0c-85454cfc8e23 | -11.57604 | -49.77933 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c75d05e-af03-382b-95fc-ecbd33251cdf | -6.10125 | -55.69472 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cc6a860-bc35-370b-bada-454a590da1fb | -8.98961 | -45.90863 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b835c5e-fe5f-31f1-b707-c504b9eeef56 | -12.21604 | -57.09008 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f663bc5a-627e-3fa8-ba81-643a3df33dc2 | -11.97431 | -57.62052 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66138d38-980f-3d00-bd95-cfceb926a3df | -13.26169 | -47.00269 | 2026-10-09 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7a6307d-dcb4-309c-8bb0-364aba809235 | -7.3887 | -44.46665 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896b86f5-dd26-3a02-86a3-af6996649eb6 | -6.38805 | -55.26812 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b62f78e-5a8d-30a1-8379-7d1b56fd9782 | -8.72963 | -45.15668 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4d93bc6-58e0-324d-b01e-de739a0b3e93 | -5.96936 | -55.34066 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fc8f852-ce0f-3ff1-a1f0-7bb49d9bca05 | -9.22542 | -45.65488 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README117.md)
