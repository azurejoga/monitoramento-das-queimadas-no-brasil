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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5f92afe-02ef-3ac5-8f52-20a1e0d67a31 | -15.68329 | -41.70857 | 2026-09-30 04:34:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 249f5b2c-b7ee-3161-a0ab-f01b77f7efd9 | -12.44181 | -44.16718 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 599ae61b-9fe0-395a-a006-555735ca843f | -9.12689 | -49.91045 | 2026-09-30 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 075fb4ad-6a28-3b37-b386-73176ee21509 | -17.57633 | -43.70834 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a5c48b5-f540-3176-b633-4d4641cf5071 | -12.44422 | -44.16675 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4feb22-1b0b-3443-b88a-e71320292945 | -9.80811 | -48.21634 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea57735-a37f-35dd-90de-77cc40d77dcf | -15.57823 | -47.89352 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb4d84a4-e2af-3894-88a6-d348288b6375 | -12.78866 | -53.99951 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ea9bbdd-2a0a-3c36-bd1b-4c5cf0e940dd | -11.1677 | -44.76959 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19ed99e-703e-31ec-b7ee-594f5f97430d | -10.55973 | -50.87312 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b7f6e4f-8520-3327-a7a8-dc14636aa3ea | -11.38663 | -43.46716 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae1b823d-4269-382c-91c0-de55bd896d47 | -11.99982 | -44.92656 | 2026-09-30 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5417be2b-b2e5-320d-9f01-8892bf6ba49f | -17.5198 | -43.70922 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 414071ec-1a72-3f99-af26-becf78879f1b | -15.20543 | -46.1443 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7aec667e-d56b-3261-ad48-12f8b095d8d9 | -13.374 | -46.8166 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4907271c-7d36-3d67-8388-875bddab5f97 | -13.30328 | -43.47142 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0858078-624a-31cb-ac75-e10a6e3a5ab6 | -15.63421 | -43.23832 | 2026-09-30 04:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d5298898-a139-38e8-8486-842acb739e18 | -9.78167 | -59.0164 | 2026-09-30 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a5e8461-6ea4-3080-a4c5-e70f58320d0d | -11.84832 | -50.97864 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 881b047e-0f4d-30c1-9949-c0723a58544b | -11.38783 | -43.38715 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60b6ddaf-38cd-31ef-ba12-01facea1c46b | -11.18522 | -45.11946 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5abfb2ff-d259-3f28-a693-c0c85ab1a466 | -11.83935 | -50.9585 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a12eaf4a-95b3-3dcd-a14a-51585827056b | -16.67492 | -41.85062 | 2026-09-30 04:34:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |
| a55b03cd-f920-3fc0-a9c3-94be2c80057d | -11.3697 | -51.0224 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1284237-8f77-3785-a5ab-821dd77fadf2 | -10.81314 | -48.74994 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2642c816-8e83-3743-90e2-2a0f678c5331 | -14.533 | -48.29789 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07404566-2ddd-34cf-9019-eca231aedce4 | -9.77572 | -44.81206 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a555a22-2760-3f64-808f-21117fc7a6f7 | -13.37703 | -44.01143 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a296e490-a3b8-379d-845e-018ceaebee28 | -9.77128 | -44.81858 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e95abba-3970-35f5-90e7-a97e2a46d903 | -12.71424 | -46.96438 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06bd4563-77aa-3b68-a71b-66342f53a479 | -11.71029 | -43.4422 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3ad6ff6-40b0-3047-93e0-887c089714c3 | -10.53224 | -51.42719 | 2026-09-30 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47de4e04-7b58-35df-b278-fb60e193545e | -11.41523 | -43.41952 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fcf6c09-235c-3895-8491-af6812592a78 | -10.5214 | -45.36435 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63f942ff-c5c9-3797-804e-68d6b646ebe4 | -13.37838 | -46.83192 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bfd31821-b266-3ba3-96be-723abff84eae | -9.78357 | -59.01772 | 2026-09-30 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24d680e1-8ecd-3a8b-a093-fd65bfdfee54 | -10.10817 | -43.92575 | 2026-09-30 04:34:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b137058d-2e64-3f52-8760-32d45312d822 | -12.70812 | -46.95971 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c0c803e-2172-3a8c-bbe7-c233c41df332 | -13.38229 | -46.82893 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d270780f-5c1d-3a14-a4ea-c628c7b2490f | -14.3381 | -46.4387 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99286a90-ade5-3bf3-ae76-d7aa5eeef100 | -9.81657 | -48.20945 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee853360-956b-3607-b9f8-c31059ae7932 | -12.24209 | -50.25983 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8eb7770-8680-39ab-9222-7168223575c0 | -11.37167 | -47.44218 | 2026-09-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eb2412a-b34a-3e02-85c0-abf89c72eaa2 | -9.81234 | -48.21289 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8e46d44-4499-3a0f-bf8f-d2f54f144939 | -11.84337 | -50.95926 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7a5413c3-bca5-3214-b9ee-310cfcb30a50 | -9.80186 | -48.23192 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab100fc4-4116-31b5-a2f8-9e36052c041e | -14.01095 | -42.91145 | 2026-09-30 04:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6e435527-226a-3151-b0cf-354818eb8079 | -10.56037 | -50.86945 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0773c1a-d6e2-34f4-8d23-8f97856cd811 | -13.37123 | -46.8125 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edafbdc6-ce22-3ccf-9e5b-ec4a02149fae | -9.37658 | -49.15538 | 2026-09-30 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d998d5-2bbc-39db-9f2a-7a1d29d7d0ec | -11.84956 | -50.97148 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b47f24aa-b934-3689-aea3-9091360c0516 | -15.63546 | -43.22945 | 2026-09-30 04:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 59a693da-3093-3f0e-818c-b64db1222e0e | -11.41173 | -43.41898 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b811d85-0723-3fdf-bb87-01ae6713714c | -10.52306 | -45.37543 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7441488-c4ca-349c-bb30-b7d42f391ebd | -12.62683 | -47.24693 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7294e105-720f-32e6-8ac7-b9a21af92e6e | -9.76405 | -44.82103 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b589c29-3e70-3aa5-86c0-9a0eb02f5772 | -11.16043 | -44.77211 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42ddf8f3-91a4-37a2-bf82-700f50fb8ca2 | -15.75932 | -46.03769 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fb8d6be-4b7a-3cd4-80e3-724d577e38e6 | -13.33396 | -43.96107 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e313c5f1-a411-331f-80d3-88c53645965a | -15.25825 | -44.81824 | 2026-09-30 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5592e385-30f8-3a8f-b1ba-d338648357df | -11.39837 | -50.97875 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5057ecd9-3671-31c1-8407-8554dfb8ab36 | -11.18454 | -44.83833 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe1e9d28-7dbe-3f34-8f7d-39ef744332c8 | -11.35581 | -50.98219 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6da79043-9ac8-3228-9eb9-c64883850cd0 | -11.38199 | -43.3782 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfbae553-b01e-3e31-bc81-5bc790a85b63 | -12.31046 | -47.95694 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 915a9c9b-7879-3108-ac0d-a36c20450d10 | -9.86091 | -44.93809 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd4b7450-6dba-3060-91c2-4e9514ea5796 | -11.44316 | -43.4479 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc983a84-72f0-363c-aa6a-ad00b19ecb3b | -14.11514 | -46.26337 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce98ab0-e6e9-3f92-9541-44b921f8083f | -14.219 | -44.53161 | 2026-09-30 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e80b3c3-3de6-3a94-bc3d-3eb471a262f3 | -11.67995 | -43.50183 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ad1ca21-f56a-3987-ab11-7575216285e0 | -12.77699 | -54.00821 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1220263d-1fef-3a03-a635-44d829d1d73a | -8.94936 | -49.79393 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f0a5b1e-70d5-3920-a81b-bacccac38047 | -10.51585 | -45.37786 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77bdcd2c-75e0-37cd-b195-4e28bf82709a | -11.8598 | -50.98446 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08e732b1-de25-3828-b94e-0be8372abb09 | -11.7097 | -43.44614 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3a4ec174-91b5-3551-850c-cab926a06f55 | -10.77447 | -47.7196 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8191059d-bf7a-3dc2-a42f-9e2efdfec250 | -15.08672 | -48.33066 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a34b1df-0fe2-34f2-af94-29887e4adf64 | -11.38106 | -51.00562 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5db63518-edd3-38c4-936e-c75ed08690c8 | -12.62743 | -47.24329 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b802602e-12dd-315e-81cd-34edfb96a0c8 | -14.12395 | -46.29406 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d2787e-435e-3961-8695-5dd191bdbc18 | -11.84274 | -50.4754 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8200a24-a9b4-35b7-aa34-57576c38caf8 | -10.71391 | -47.82761 | 2026-09-30 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40d32bf1-ccd6-388f-bd62-9acc9709d83b | -11.40882 | -43.41452 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e0ea269d-4a8b-3f30-a1d2-f7b68c245a18 | -11.86042 | -50.98087 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 448bd42d-a225-3741-beee-d05c422b6c7a | -12.25498 | -43.48116 | 2026-09-30 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f896bfec-1b71-33c2-9e36-19ce912ac860 | -11.51999 | -48.32112 | 2026-09-30 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 436ed0fc-78a6-37b5-a99e-596f759e5e6b | -10.89985 | -56.17936 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e06a38f-50fb-3163-9fc3-20757dda0939 | -10.52362 | -45.37191 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3979a5d9-a0c7-303d-b998-84da71dd2dbf | -11.83532 | -50.95776 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fae7a53a-648e-324e-b64d-f11953053bbc | -13.17801 | -48.53667 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292f5bfb-9168-39ae-bfb2-7bcf0b724b6e | -14.0116 | -42.90705 | 2026-09-30 04:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 33.4 |
| c0a75af1-bf69-3c5b-a82d-22c4210217bd | -13.33639 | -43.94899 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994b5706-33ae-33d8-bce2-1c8734dad2f2 | -14.50814 | -48.27821 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 620f5f2e-8cdf-3a0d-a196-b023b81e7828 | -13.36952 | -46.8231 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c7a3e24-e66a-35e4-9347-bd94fbdaa5e1 | -10.51805 | -50.84615 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cb6e02f-dc1d-3f80-b5e6-75a999f36ab1 | -12.71702 | -46.96848 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e160395c-ab58-3e9c-a5c6-51a325de9af0 | -15.63483 | -43.23389 | 2026-09-30 04:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b7cda9ec-eeac-3bc4-b84b-8792536ea3ae | -11.82817 | -50.47006 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede618b8-671a-37f2-b789-d2e2d500e192 | -9.08614 | -49.88772 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a5808a5-eda9-32a2-a2fc-90c71ccb15a0 | -9.81167 | -48.21691 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
