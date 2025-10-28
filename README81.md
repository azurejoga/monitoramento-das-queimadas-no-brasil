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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f78892f7-bb42-32b1-a900-f53837bb1f91 | -5.82821 | -53.44653 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6e535a-9a87-3509-a698-d79f8bb1bf82 | -12.69846 | -46.31879 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80130f07-6412-37b2-ba5a-6a1cb73bf01e | -9.21805 | -46.34771 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46482870-6267-38d9-b591-42e56feb0dfa | -8.19706 | -46.93948 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdfcb63-aba2-3aee-ab3c-af2d00f9e8be | -7.67782 | -47.42065 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0352b0ab-d4ba-33f0-923d-5fa9b1ebb5b4 | -12.0851 | -45.67788 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57408170-a03d-31a5-a81a-03e2ca1b2c86 | -13.24231 | -47.06067 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39d5f287-cc2d-3537-b55e-0d1f45189a49 | -7.82252 | -46.42023 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 035f0268-88ad-3fc9-a81f-e5ba2aa79e24 | -9.53504 | -46.97302 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 949fbf08-1248-3ae9-83e4-0fc547e6e73c | -6.58289 | -44.62555 | 2025-10-28 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 537a36ae-5b1a-36ce-86e1-65c057f22b4d | -10.58176 | -49.80298 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f166cfaa-26da-3461-aa8d-190a22819989 | -7.94163 | -45.51561 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d37d3901-a005-3a6b-ab1e-ec1ea4e5f5c6 | -10.64582 | -47.90818 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5265701e-9d4f-3a51-8718-620f07102bd6 | -9.2124 | -46.34719 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b968758-5bfa-31f0-b8b8-1b492586caf1 | -7.8129 | -46.4441 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba8f9201-dc8f-35db-acf0-86b45d3c2138 | -9.22276 | -50.20751 | 2025-10-28 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f8360f-22b0-30b4-8019-7dad7bb88cd4 | -7.96224 | -45.53959 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8722d214-d8dd-3be2-9f24-e769712b2c7b | -7.80907 | -46.47951 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e29ab0c4-5f5e-365b-82f5-f1e7d8fbae20 | -7.9742 | -46.7412 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18186d01-9bff-366f-b605-a862ff70919f | -7.97468 | -46.73779 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff70253-c75b-37f0-8d03-af7df04cd245 | -10.9666 | -47.82318 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 979852fa-1965-3d3c-96c5-b3b816c22ee4 | -10.56255 | -49.83157 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3af2d67d-e6f6-3dc7-8360-2acc8b5ab434 | -8.08169 | -45.96467 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f54d78-a01d-3410-8059-c7d37017399f | -13.63718 | -46.46786 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c24f4c-81d7-366c-a817-b670afe0f9ce | -10.33047 | -47.7841 | 2025-10-28 05:04:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| be6cab00-f04d-35be-a4f0-4585fb8ea3c0 | -12.97747 | -48.3899 | 2025-10-28 05:04:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c28a10d-058b-36ff-83c1-096f3cf60508 | -10.30932 | -47.16117 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36c893e4-1ddf-37da-aa61-6703c98d8f86 | -7.89179 | -45.70898 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1d93be1-a051-337f-b67b-a40c33b4cc5e | -7.83395 | -46.41841 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c7eeedc-cf8f-3eea-bc2a-406994dee69c | -9.88739 | -44.89541 | 2025-10-28 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1612dbcc-2a66-37e2-8c4c-84ae1d1812e6 | -12.18762 | -43.59068 | 2025-10-28 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd594d8f-c0d8-373a-88e2-53dc5db4a5f4 | -8.16228 | -47.00478 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb912177-ecc5-353a-97a5-faa001939512 | -7.93208 | -55.01949 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4544c9e1-5066-3def-bc68-1645a2015968 | -8.25187 | -46.89649 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9b92e7-5d8a-3a60-8035-ce97a82ed1cd | -10.33086 | -47.78109 | 2025-10-28 05:04:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7eb9d4a-15a6-3b14-b2b4-9daf53466162 | -7.26257 | -45.01587 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7f8cb88-520c-3d55-bc21-fa4dde57cfc7 | -9.95897 | -47.09546 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d249cb72-72e2-3d43-9a22-1a1bc67206eb | -10.93488 | -47.65625 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feab391c-a111-3cc3-b61d-07c015e97e04 | -7.98855 | -46.73666 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2657d420-89d3-3512-8271-3bc54cb0ad0f | -11.2821 | -45.51324 | 2025-10-28 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 62157c44-b5ec-3122-be68-8f1d269e553c | -7.81417 | -46.44106 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3bde694-ca45-3ece-a46d-829cb565393a | -9.21948 | -48.60128 | 2025-10-28 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcee565b-59e8-3084-a72a-0dfc1f337467 | -9.47275 | -46.90002 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41185e33-1b89-39da-a2ec-e79ffc72556a | -13.37544 | -43.45782 | 2025-10-28 05:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75601024-5cd6-3d25-b0ce-3d50e2991906 | -10.52375 | -47.73325 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9618182-dd56-3c53-9287-4cea9badd60b | -7.27566 | -45.00894 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59248a3e-c3ff-3ec4-8f07-196486f8af07 | -7.96785 | -46.74741 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22fd5305-2fb9-3321-8248-9e7ca8106b83 | -9.26992 | -45.57616 | 2025-10-28 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f75e066-feb1-3327-991f-eff3d9da8220 | -7.97143 | -46.74165 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d720e743-ec29-3552-80cc-29ff107066a6 | -7.25542 | -45.00349 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee52e8be-e720-3a35-b7ae-0ef564df48d1 | -10.8801 | -48.37784 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2cad3d7-acd1-3056-b12d-d67fbd6b0b7a | -7.16135 | -47.0034 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbd04f06-c380-3bb5-a3b2-b54944cf1755 | -10.36517 | -47.16984 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92626291-4cff-3573-ba15-780560ca7f21 | -12.62768 | -45.08445 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e786af67-087b-3bf9-9bfd-cb388568780b | -8.1618 | -47.00824 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac43e08-cb6a-3aed-b058-a15710b77a82 | -9.95039 | -47.10346 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa8ab8cd-46b8-3f56-a560-52cb2085df55 | -7.81545 | -46.42589 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 570c8d0a-0708-336b-8914-150fd898a592 | -7.97373 | -46.74461 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e537d8d0-e8bf-37ec-91fb-9cfbb640242f | -5.79613 | -49.83039 | 2025-10-28 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2018eaa-8d48-3b71-9cec-381b1aa790bc | -7.30807 | -44.10592 | 2025-10-28 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57a8a24c-3272-36e7-9666-e7c4a60f8037 | -10.36562 | -47.16625 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf6ea33-8fde-33a0-afc4-2322dd4d2031 | -11.15844 | -47.78408 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1a86367-6453-33a7-a3cb-38a84adcaa75 | -10.75749 | -44.75969 | 2025-10-28 05:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fbbae72-6a57-37ac-a613-95ab62e6a5a6 | -10.58672 | -49.76579 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab7d54e4-4fd3-3ebf-9e51-b9d7283bd68c | -10.29676 | -47.17334 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40654bc3-1f2b-37f4-b45a-1915b9124269 | -4.96535 | -56.27328 | 2025-10-28 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a3d17a1-2da5-3ff3-b590-c64821ca3810 | -9.8754 | -47.46331 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a16bb1a-edd0-3dbb-95f8-d1f46f6df1e3 | -7.26615 | -45.01394 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31ac2d0e-3766-3b37-acaa-8265be3b0c71 | -13.62955 | -47.03828 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66a0150d-435f-3f2f-a65d-9b2c91d7b271 | -8.87446 | -50.33461 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6efd27f-778d-311b-bf76-4575c5230952 | -12.62094 | -44.25247 | 2025-10-28 05:04:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00074444-0f37-3e2a-8716-9db2b3d4b62d | -10.56611 | -47.89991 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48ed0c74-4cc7-3bd1-8268-73b3767f6fff | -8.18771 | -44.44834 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0a1cb63-b2d4-3377-9931-0e91b357c9e3 | -7.4888 | -47.03448 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b366c5ba-b87f-3550-a57b-cbafc52a62d7 | -7.98698 | -46.19761 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45f8037a-e76d-3517-b113-1ccbb5c00fff | -9.53837 | -46.94818 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1555c95-8932-3333-81ac-8544d3c1ae15 | -7.94855 | -45.50812 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 129a922a-c8e8-3535-b1ed-cedacea47cec | -13.36995 | -47.39212 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e061b59-6771-34c9-bd81-a705136e6eaa | -9.53808 | -46.96265 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0f95174-d5b7-3963-b3bd-efa58aaaa52c | -10.58754 | -49.79433 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f3dcab9e-b954-348e-8b1f-4a65d8fdc801 | -6.60535 | -44.64219 | 2025-10-28 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3e71614-511c-39b5-bdf9-fa19d9befce8 | -10.94442 | -50.27271 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 821141b4-50dc-3926-aa53-6ee82e6479d6 | -8.19224 | -44.44292 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f8743bd-e055-3a94-8624-7d815f718cbc | -7.94745 | -45.47098 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99054a56-2ac4-364f-a229-df2802a4ae25 | -10.28919 | -47.1897 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1918f3-ddb7-380f-95c2-eef62600df91 | -12.19934 | -46.50805 | 2025-10-28 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bf9d890-0450-3bc9-a03b-77f8c2d36a49 | -7.97549 | -46.75245 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec975e3-3987-3f6e-a0b2-d4368a29c513 | -8.56936 | -47.02783 | 2025-10-28 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 522b7049-e947-3284-a32a-9bc03988da5d | -9.99345 | -48.10653 | 2025-10-28 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1fae785-313d-33b9-a7b9-7946724ccb72 | -7.85984 | -46.39249 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72933da3-d8f0-3c70-9c31-a2945060fd0d | -10.2959 | -47.18016 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad331f7-83bf-34ce-b4f7-d02db6844529 | -7.06867 | -47.36591 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43f3438b-052b-30cb-9f32-feb271057ff6 | -10.58362 | -49.78905 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd4d9924-c6a4-3fc4-9e2a-77ef2d4ce01c | -8.19467 | -44.44408 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ae1accb-1c8e-3290-8f35-c0b53d502ce9 | -9.46201 | -46.88538 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 188a6269-b1ba-32e5-8e1f-d7822f7ec8d3 | -11.07452 | -48.32928 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f558f2af-b49c-3959-a293-d0aefc3e7987 | -13.37032 | -47.38893 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0985e6df-24ae-388e-90bf-99ca92f9b251 | -7.26875 | -44.96906 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b686d15-8d8c-3e50-85a8-bd5806e79631 | -13.23077 | -47.10891 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0607efa8-4aea-31f6-8272-fccd57b1721d | -7.67434 | -47.42493 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README82.md)
