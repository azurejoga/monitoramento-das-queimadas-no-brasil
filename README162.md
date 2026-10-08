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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29235a4b-0eb2-3629-9798-21065a2fa8c1 | -2.98722 | -56.59401 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eda1c12-6d4b-3ce9-9348-a67efb879015 | -2.87204 | -54.20006 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd277a64-4f09-3339-90a4-5191e56fefa2 | -4.13101 | -54.26021 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815cb346-2ed1-3b71-83c3-15115049df13 | -4.26734 | -54.87206 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d3a0a8-8632-3f9b-9c24-d637eead884d | -9.16567 | -61.4087 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ab832be-d4b6-3d98-955d-f244ec930d20 | -3.35526 | -50.48109 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab08e5a1-19e4-3df5-8e9b-2c3120defe44 | -3.07513 | -54.26178 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3f2a3e4-0e9a-3d79-a0aa-22442b791e45 | -3.3646 | -50.47834 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14bc8fe6-c418-3f43-80ec-a223062355a4 | -1.47793 | -53.61832 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b205343d-f932-337d-ac6a-b4704dee5af2 | -1.42348 | -54.60952 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61b75ab4-3340-3b54-9e3f-8e2ab30a4f09 | -3.64009 | -60.62993 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65e1f5e2-1db2-318a-b24e-ad5fcfd4a899 | -3.0486 | -54.15266 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37526475-af41-36ff-a3ba-626284554987 | -3.73714 | -59.44847 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7cbe53a-e332-3996-a0ee-f4c14cf3a21a | -2.98091 | -54.0313 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfd59f43-e963-33bc-b2a9-095fba175ae8 | -2.78441 | -54.0694 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a828b6d8-96a4-3967-b2e8-1a07ce5bcbaa | -3.18156 | -50.55914 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecfbd2c1-18dd-386a-aa81-cf3e6907fc47 | -13.17538 | -54.31826 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f356a4f9-be5c-39bf-b072-6da2d99ba819 | -3.52517 | -59.33003 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f4b540-48d9-3e43-ab99-76807cb51947 | -7.3929 | -55.20416 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d18927f-4067-3cf9-96b6-5b3b2f42086e | -2.94996 | -54.20431 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f83448c-e8bb-33ab-92a6-1d0f05d9f92f | -2.68703 | -49.04998 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d73fbd8-8e84-37d4-9628-cec047ffcc23 | -3.73291 | -55.98737 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8420c618-7e7b-3126-ac08-7128700b2502 | -2.36254 | -48.87961 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffeee95f-b3bc-35db-bd74-84dc5525bf9d | -11.31766 | -46.68681 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a722a42f-279f-3b4a-8f73-90010bfefd37 | -3.58215 | -54.66206 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f89ce4ec-708b-318e-984f-3210a94147a1 | -2.99997 | -54.05001 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78c23b84-786b-3c50-b360-bc88806c20ce | -3.79993 | -59.36724 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 408787e9-205e-364f-b313-26a2487e2a7b | -7.22886 | -55.12131 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6380d6a0-da3a-3dc8-8d5b-0678ad07a6e5 | -3.67575 | -54.50229 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8101c1a2-aa2f-3cd4-985d-1cf45defa8a2 | -3.08705 | -58.00938 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88b97096-e3f5-35ac-95fa-6eaefcf88956 | -2.871 | -54.16053 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca14beef-4a32-328e-ae74-204e0af6ebd8 | -3.08144 | -54.29015 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ddf3228-b646-3163-8cc1-ee37e0a616fd | -1.27161 | -55.39855 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a6f040-ffac-33bd-a335-19eac27d50ab | -3.08492 | -54.29069 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0fd81f6-d69b-30d6-81e0-a55d6cb11876 | -4.11259 | -60.71448 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ba66ca1-0517-31b6-965b-55f050012114 | -3.02784 | -54.10197 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 123a343e-ad5a-368e-979d-418a53dcb096 | -3.38639 | -59.42796 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7dd1c1d-1cfa-30d4-aa76-0658abbb3f0b | -7.2153 | -55.16274 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd10410c-1760-336b-831b-cd4af19e5167 | -3.58754 | -54.5592 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f5c1c3-b674-3f89-a65e-b921a26d1165 | -3.10447 | -54.18775 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aad7bfc8-f574-3084-b060-5f490faffc80 | -3.44049 | -56.935 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3edf93b0-6805-3574-ad3c-df3687aad512 | -3.50557 | -54.63924 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ead3ba06-b920-39cd-ae2d-26b211fd0ec0 | -2.57742 | -56.16831 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21905dac-92df-3af0-ae1e-621def411d00 | -3.11255 | -53.76878 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c53325a-4f6f-3b38-876d-383997c3b5ae | -6.21401 | -52.87611 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7b81f83-80d1-31e0-96cf-28b6f5e20d33 | -3.14573 | -53.72053 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ea35e5e-5717-31a8-b06d-be8a7c347e51 | -8.54792 | -67.07626 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 655d89eb-9c67-3011-8cb5-42fcadc4f7f8 | -1.20905 | -55.6912 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18dada75-91ac-32c6-9c1a-3e597e335949 | -3.54536 | -54.67168 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3c437ea-bcc2-3cd6-a213-376ff0a67dd5 | -4.81142 | -54.67873 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9ea0307-573f-3530-9b72-d321b2e0fb12 | -3.24361 | -46.9551 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b53db13d-e8e9-35d3-8583-300882731732 | -1.53352 | -54.55184 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 44bee66c-b8f6-34df-ad8a-963b1a8ca3ec | -3.18673 | -58.65165 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32ece7da-7b74-32b0-809d-0baee82266dc | -3.50094 | -59.27722 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 446d22e6-3fdb-3cc4-9ac5-0d588a864a6a | -5.72693 | -45.1608 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fbc96f7-92b3-3ffa-92ff-cfa9d51fdae6 | -3.0181 | -54.18733 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f779a74-dec7-346a-bdd5-8d5550594c7e | -3.0503 | -53.95787 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a3c47e00-9d37-3f89-a0b4-6560d259b0a2 | -2.48633 | -56.12587 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcf160ba-daeb-397d-9809-5abc589ca23d | -3.27418 | -54.07054 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8263adf2-098f-33fd-a36e-d776477f6f1f | -3.07977 | -53.95439 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5a362eb1-e00e-35f3-8e7f-f07f59fe89e7 | -3.0622 | -59.26783 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81c54d23-2d6f-34a3-87ae-45eba51a0886 | -4.4251 | -59.49451 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f912a99-f8b1-39aa-8a74-244c62ae1c34 | -9.48538 | -64.34948 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a0ad87c-aab3-3438-9a2a-526f4aa91e22 | -2.76446 | -54.10574 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7b587cc-c42f-32a8-84ed-213bdd0f41ea | -3.84264 | -55.97934 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8fdb2e3-efe9-3e49-a59b-4084811c1dfa | -2.97612 | -54.12959 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6da438-d172-38d3-97ab-efb4196a13af | -6.46494 | -55.47911 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cd6419-7e5e-35b1-bbc0-a7528748ecab | -2.77562 | -54.0799 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f137d69-fa52-3946-96bc-94c7f090db98 | -3.05228 | -53.92197 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b7b3a62-61ee-3a40-92f0-52c4cf24532b | -2.76403 | -54.10259 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a0e3cd4-1198-3ede-9cd9-a57182316307 | -6.87792 | -43.68809 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9d1af3a-7136-3d39-bf4c-7b10135a2fcb | -6.73096 | -55.10683 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f54304b-2742-3d8e-ad2a-7b9a32525b84 | -2.97201 | -54.13286 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 402b18d8-2cf2-3150-81c3-c79e095b59f8 | -1.46766 | -54.63831 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1bc5484-6e73-3ceb-adca-9d464063a6ad | -8.53085 | -67.04854 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fd4d8ef-ec93-3049-8f13-de59502d6e59 | -3.82618 | -55.77924 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 212ddb22-73ec-3d75-b181-5e33da337ace | -2.77502 | -54.08375 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2af3223-4ae3-3a43-bc13-b7b9f5e01be3 | -2.68716 | -49.05151 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f17595df-1652-326a-ae32-7d3e5da685e2 | -3.25916 | -54.02822 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7a121ad0-4f7a-3b69-ae7f-f242f75c7588 | -3.54577 | -54.65311 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d05c2d14-6bc4-3fd6-9526-63f0b4397fe8 | -3.22667 | -53.89104 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f7f1dcf-1226-3ec2-9e5d-53d70953fe75 | -3.27739 | -54.02705 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a27dbf72-c93e-3e95-bfc2-438616a758b6 | -2.4897 | -56.14765 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b977683-d50a-31df-93f0-bd3d14efb68d | -3.62796 | -55.50935 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6898b5a-5ce1-3789-92c9-5185129a78eb | -5.73407 | -45.15671 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a3e4cc8-082b-34e9-af64-523c1964feed | -2.58294 | -56.15501 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac7ab24a-1448-349b-96e7-3cc99e386008 | -5.92247 | -55.69323 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75c88512-35b5-3414-8170-853a70efd429 | -3.29071 | -54.05716 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 060d2706-d0f3-3f72-bbbb-6b71b0bcd7e9 | -3.29714 | -54.06214 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec8fcd7b-3859-36f9-986e-a68ba34a992d | -6.11606 | -55.70462 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6c8afb-16be-3662-a163-24e2c43a6dee | -2.94231 | -54.11656 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7687faca-9a81-3f52-a488-d0b6931c9b72 | -2.77265 | -54.09913 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 862021c3-3ce3-3058-8894-33cdb339dbfa | -3.25314 | -57.86918 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6002ffff-6b20-3fd0-b49b-d1aceebfce27 | -3.06367 | -54.17076 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a55045d-a5b3-3343-b294-e3c9d3b9bf6c | -3.5032 | -59.28573 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0813923d-5351-3fc4-bad4-b110fcdf2210 | -2.88217 | -54.87689 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d14d7a-0452-37d9-9782-7c6d13c1b141 | -3.12093 | -53.76189 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c6c2778-121f-3040-af8d-66ab9cb88d17 | -4.34646 | -55.12959 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd138a4-5411-3805-91e3-9310e080598c | -3.26766 | -54.6869 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e9f894-f57e-3164-94e4-1f7005527124 | -1.52501 | -54.53934 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README163.md)
