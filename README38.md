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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c194adbd-9bd3-39b4-ae2a-d1aa74b4f891 | -12.7092 | -46.84616 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0e941c2-a7d1-3859-b125-42afe6fd3876 | -12.69972 | -46.83773 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2609925-fd8a-37d1-aa5f-75fc66d01ab8 | -11.28652 | -47.50555 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b03a5ce1-fc8b-3f61-946b-9422524ba056 | -14.4552 | -46.5174 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5c0bff6-ed81-3dc8-ac73-9a6d9edca27c | -6.33906 | -56.19133 | 2025-09-21 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48d5ab48-ff15-3ca6-b399-5d2ef89e9c30 | -12.34991 | -43.75743 | 2025-09-21 04:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23934fd9-5add-3323-9643-50f9500a392b | -11.49015 | -43.57593 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 782df320-b392-3527-bd89-8b4ce4e58d9e | -8.98593 | -65.4475 | 2025-09-21 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15a6d7e2-5f0c-3cb5-8727-5d1d744c6e1e | -9.73823 | -48.08487 | 2025-09-21 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 887bffa4-46e6-3aab-bcba-168d4d77cf56 | -11.31136 | -47.50384 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ac89633-5bb9-3667-93f6-f7ffbbc65147 | -14.43146 | -47.5749 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 353a9031-9b67-3644-ba48-975009d35725 | -14.46918 | -46.51234 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b43752aa-4a27-374d-ac24-ade35de277da | -14.6301 | -48.26948 | 2025-09-21 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b44dc592-b932-361a-9a36-6100411ed0e2 | -7.93715 | -44.10424 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3d3e00b-dcaf-3162-b4e0-0f7647c21bd0 | -12.70741 | -46.84449 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d195716e-8e61-343c-a8bb-dc4729f6b9eb | -12.70446 | -46.8419 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 212ad536-6b00-3336-b579-baf9d371b658 | -14.4361 | -47.57335 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 867b6360-4457-3705-9f96-df9c9eb80e1b | -9.42406 | -44.71635 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47f9d769-b0e7-3420-9f33-5d90b7535fdf | -7.94282 | -44.10878 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 113ec755-955d-3ce8-923d-333dc9017aea | -11.49866 | -43.58843 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb346d40-933d-3977-974e-8473342e7b7c | -14.43834 | -47.56084 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 484a6f0c-5a19-39fa-a995-1635bb417ff2 | -12.43269 | -45.13119 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4ab8df2-e3b9-3a51-85ca-482691af44d1 | -12.06851 | -44.82441 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cb0e0ed-1189-3a18-8103-25d6ba9aa42b | -7.93702 | -44.10799 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb543b38-a97a-34c8-9ba7-5c88ac7f385b | -10.26195 | -46.05486 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 426ae5a2-c3fe-3a26-929f-8aff106e2986 | -9.42513 | -44.70812 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d05a786e-c105-3f8c-a251-6beb18f27948 | -14.45559 | -46.51416 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 921ec939-4265-3384-81e5-61716ca6398d | -10.34334 | -45.23706 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88160b4a-f276-3c92-a14d-eb7d4f8696f8 | -11.27922 | -41.85584 | 2025-09-21 04:57:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e444c573-011c-34dc-b37a-006bf9c7d410 | -11.48894 | -43.58596 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b65c748-75d6-384d-8e33-3b92b8889296 | -10.32909 | -47.87221 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ff978c-9ba8-3f95-837b-58aef30b6c10 | -9.43085 | -44.70864 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e32c5c-241b-3e99-a741-3e8e2486b2a1 | -14.52497 | -44.87305 | 2025-09-21 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69d95598-502e-3928-9984-466aaa02d695 | -13.31265 | -47.27892 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d68e2b78-aa80-38d3-973a-52b087909861 | -14.43105 | -47.5728 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5efb2bd-0117-34d7-884b-09c486c164eb | -12.71003 | -46.83925 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80340a50-ce70-3998-9d37-a667d58557b9 | -12.07285 | -44.83752 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 676f3012-4011-327c-a7b9-386fab47444c | -14.43748 | -47.56167 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19cfbb9e-3254-352e-9d4a-e0c3af88e7f0 | -12.07232 | -44.84183 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deab372d-d082-3d10-8443-33d9137a255d | -13.24786 | -44.1166 | 2025-09-21 04:57:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e641464-0deb-384f-b073-d65d72a921a8 | -6.33966 | -56.18757 | 2025-09-21 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e32d324-4b82-3295-a3db-e725afbec534 | -7.93658 | -44.10841 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7838626c-afd3-3b7d-a481-78c98c40fa76 | -14.459 | -46.50548 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 332d536e-12ff-35d7-92a2-678e869f514e | -13.53968 | -43.00298 | 2025-09-21 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 45.9 |
| c150d697-dbe8-3564-bd27-04dcfcc0b155 | -14.45012 | -46.51406 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 115fe462-e3ec-3222-a730-a7774e6797be | -14.44182 | -47.5682 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a3fbe9f-6074-3971-8579-d6792723d8ad | -8.20532 | -61.20229 | 2025-09-21 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3188b8b3-a0a3-32c1-b1ab-babac316c9f9 | -14.62531 | -48.26867 | 2025-09-21 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28169db5-11cf-38c1-b3f7-8622280a29d0 | -12.41834 | -45.10421 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29e5f8d9-7714-39a9-bd77-cb59f8359dd8 | -11.28962 | -47.40643 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05681adc-34a1-311b-9a66-d4a98e8c2628 | -10.96223 | -54.10089 | 2025-09-21 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d7b5493-0733-3829-8995-27232fc38ac0 | -13.35999 | -44.28287 | 2025-09-21 04:57:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 213e01de-7580-3ea0-8e6a-1a4c0cb1d88e | -14.43712 | -47.56472 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 518007c6-23ae-3df9-9a82-6ee604a6bc71 | -14.25616 | -44.38758 | 2025-09-21 04:57:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112dc5b8-e061-31f1-9a1f-7b16faf05075 | -7.93176 | -44.10298 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 109a78c4-2af9-3d56-91eb-55874025ca8a | -11.20536 | -42.19138 | 2025-09-21 04:57:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d218515-623e-30d4-b3f2-c30c84f6a62c | -11.29453 | -47.40673 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37dfa5da-18c9-30aa-b63e-32b55fea6b9d | -10.04191 | -46.26869 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a615e34-957b-3221-b444-60e1e228a287 | -11.48607 | -43.58715 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42d22b2e-72d0-3d1b-87f4-db27605b2ea0 | -13.64567 | -45.70047 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd82593b-2085-3888-aa8c-425cddf9cb06 | -7.94181 | -44.11332 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b33cbfe-1f20-3016-928a-3390bb6ffbb2 | -12.71076 | -46.8592 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba04bd64-34de-38dc-adee-a8f29d0a77ec | -10.28582 | -46.07727 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9d02ab7-a7e1-3469-a22d-ea26c3a8b494 | -10.40036 | -57.95493 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cc8d942-997a-308c-973f-37e91e84b126 | -7.92651 | -44.09796 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94c331c4-0ac1-34b7-90fc-263e57c582ac | -12.31867 | -44.84919 | 2025-09-21 04:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd6da22e-18f8-3261-9be7-e57b7dbb4191 | -11.02179 | -44.65199 | 2025-09-21 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68957084-a9a4-3db5-b152-f0592e145a3a | -7.92152 | -63.49348 | 2025-09-21 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 335714ef-e06d-3931-85db-080eefe67f6d | -10.34901 | -47.88736 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd7ed11b-a689-3027-b06b-0dd111281149 | -14.47539 | -46.50601 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da917e4b-ec1a-3312-8af4-fd98b9dfb625 | -8.98259 | -65.45821 | 2025-09-21 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cf6e4dd-e9b0-36fe-8974-4907a0fc7244 | -14.44254 | -47.56213 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f41b1108-733b-3578-b06a-12f3804bdf63 | -7.93601 | -44.11256 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf29dd39-3c2d-3501-8fb7-9c7187dd61ea | -7.9381 | -44.09965 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f49fb25a-88f6-33e0-9ea5-6425013caefe | -6.47067 | -55.8967 | 2025-09-21 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ac15654-d3d1-38be-88f7-de7417bfb907 | -12.07334 | -44.83349 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20140bb6-0f17-3eab-b8de-e5fed71f50a0 | -11.30514 | -47.51362 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51a3ca2c-f022-3cdf-9eac-9093db20c5f9 | -13.24971 | -47.21403 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bdb5c50-0115-37fa-9b27-2d8164968c90 | -14.46375 | -46.51188 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a453b43-b8df-33d1-bcca-efbf3c71e370 | -11.49137 | -43.56578 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e13ab68b-fef3-38cc-9c49-9198c2bf9478 | -10.34888 | -45.23151 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f89374-c8ba-3d64-97c0-6fded1cddb1a | -7.80451 | -47.6039 | 2025-09-21 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fe7c0d4-d1cb-397d-b855-fede6ac4cd3e | -14.17026 | -49.10267 | 2025-09-21 04:57:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb5535d2-069c-3584-9f75-f6886432690e | -7.82799 | -45.62675 | 2025-09-21 04:57:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6f94404-20e3-3ada-a09f-0880e0d27dd1 | -12.0718 | -44.84617 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8395c6da-fdab-3504-b8e8-9c01e9a2a2c5 | -12.7203 | -46.84108 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 191dca98-4496-32cf-92e9-a4810dc1efed | -13.24937 | -47.21677 | 2025-09-21 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53a4f53f-ab66-3c1e-9f4b-1768421b619d | -10.35764 | -47.89365 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d22e2dc5-8e1d-3962-badf-325bce24040d | -7.93078 | -44.1076 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1c006db-cea8-382f-805c-07f10bb18816 | -10.34433 | -45.22951 | 2025-09-21 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62ae3e96-dd3e-3633-a155-92541f758510 | -11.77759 | -43.77065 | 2025-09-21 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c2ef964b-515f-3f2d-a229-2a177b82f19e | -8.35371 | -44.70762 | 2025-09-21 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd96345b-ba0d-3826-a573-3b33d20eafcb | -11.30443 | -47.51892 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc8d75cf-d90d-3a03-8293-e58556bf6159 | -12.89333 | -46.77197 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 085c64be-7be5-3330-b1fd-88702ae6f3f1 | -14.45674 | -46.50465 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a0bb142-53d4-3d1d-aea8-547e9c9f22ca | -8.20085 | -61.20149 | 2025-09-21 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb32d201-0c58-3b73-9406-260f711ae7e1 | -14.6088 | -49.76281 | 2025-09-21 04:57:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc0d3d9-be30-3757-9124-cfc05b9a5274 | -11.48721 | -43.57709 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a849158-8e61-35cb-b4c9-552501f7bcdc | -11.29864 | -47.4132 | 2025-09-21 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65226330-1d6c-3d7b-9bb0-2dc4ef493cff | -9.16233 | -44.62785 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README39.md)
