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

## Dados Diários - Página 266

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19e76c30-9494-3183-96fd-517b6e58d5ff | -12.34417 | -47.31508 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9ed4d82e-ed62-3e90-81d6-bee6412ab6bc | -17.15623 | -39.43443 | 2026-10-09 15:58:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| daf3e233-4761-3b1c-8f35-3a69b57d2dce | -16.13041 | -39.01015 | 2026-10-09 15:58:00 | NPP-375 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 2fb19e3a-0067-3734-bde3-b12b20057d19 | -17.28737 | -41.22058 | 2026-10-09 15:58:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d1522d3c-18b8-3b4f-834c-512859d2d5a4 | -12.00748 | -43.44138 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3998633d-5503-36dd-9ef7-0763959f208a | -11.99941 | -43.46001 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8f58daac-e9d8-30c2-aa75-afe7a99885ae | -18.08875 | -42.26315 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d7536250-807c-3727-ba66-1361964f4eaf | -12.14951 | -44.72073 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 66a4c699-8ff6-3ba3-9d1c-577936fbeafe | -13.10684 | -46.33579 | 2026-10-09 15:58:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 216c2c9d-9dcf-3027-9cd5-9d974448eaa3 | -11.98101 | -43.46141 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 51d8fbab-5504-38c2-b59c-ce3ed633522c | -11.77946 | -46.80786 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| d7dd5c51-a74a-395e-b2ad-57b7c8bd9b1a | -12.05336 | -43.42673 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1c4fc7bd-0526-31fd-abf8-295122c6b58f | -16.93685 | -42.10885 | 2026-10-09 15:58:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ae53a20c-ea19-382d-b5e8-408dd928dc6a | -11.65688 | -43.6983 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f5016350-d708-3719-ada4-baaa2c6afb6e | -12.20089 | -44.62208 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 16b14324-8342-3208-913e-b1098e882d07 | -13.40564 | -40.78366 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4f70e80e-a444-3e82-a11b-75828926cb14 | -11.76602 | -43.5301 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f65f06d-da73-3622-a17a-c917055c6173 | -13.585 | -40.01724 | 2026-10-09 15:58:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4c06865d-c43b-39e3-9928-f46fdcb97bc3 | -18.32855 | -42.37129 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 1113b33b-0ccf-3765-b896-5789fdc61e12 | -12.05241 | -43.41879 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ed518f93-4a9b-354c-9d4f-be06621a787d | -18.26894 | -42.35785 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 38b191d7-545a-358a-a9ad-64bd1f088a7c | -11.96627 | -43.48316 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a9497e61-66ae-3a4e-99ef-c546d4b33a47 | -11.47429 | -43.39371 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47961b66-c0f6-35f3-9653-44427552c407 | -15.26229 | -42.36053 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 1865c630-b50d-3274-9362-4f8614fed690 | -11.46819 | -43.39053 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 50afba81-c245-3a29-b7c0-491f02395a2a | -16.08172 | -45.96687 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b2dad0ff-db7e-357c-89f5-6c7a33e022ec | -11.60548 | -43.61583 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| c6de1ab4-a6ef-36b8-a463-2f67ae6c64aa | -18.31716 | -42.37388 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| 69fe370b-7b7c-35bd-828a-b048750cdadf | -14.66924 | -41.79517 | 2026-10-09 15:58:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 47bb33cc-b2d4-3235-a436-4e056c15fb4b | -14.46586 | -41.95207 | 2026-10-09 15:58:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c2599c78-88a0-367b-9c3f-ebecb04afdb3 | -11.89313 | -47.38608 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bc7411cb-6d1b-37f7-bf3e-5020f0db3fe0 | -12.37122 | -46.56704 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 69253227-e37b-3bf1-84b0-56d5cf71e845 | -14.43498 | -43.92786 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| d727c146-05b6-3211-863e-7487afb287a9 | -11.98153 | -43.46571 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| b8f3329e-8c34-3f45-8c5f-20be8a3130d5 | -18.31675 | -42.36991 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| f9922ad4-1a50-37d9-b7be-f35da7884b6d | -11.77153 | -44.96336 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b5914791-11c0-3c50-b363-2d043b8d921e | -12.12284 | -43.31177 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 29cabbbf-a49e-39e0-8eaf-52a767a912b6 | -14.58617 | -41.2046 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b9db6248-7241-3b1d-930d-15b30852f4c1 | -11.60566 | -43.61167 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a75c3af1-feaf-310a-9235-3268b91f5cbf | -11.83267 | -43.59404 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 727b7c40-8168-3f90-a7ae-fab920537afc | -11.83937 | -43.60136 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 535743c8-7f8f-3651-adb6-f197f87db53a | -12.22224 | -44.69767 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71f705de-9979-318f-9b5d-679d58423e0a | -15.91869 | -38.9689 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ea46002e-4045-38f4-a6df-5abff1a35bfe | -14.77414 | -41.46354 | 2026-10-09 15:58:00 | NPP-375 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 415c90d8-153e-3fae-9c21-bcb882baf134 | -12.145 | -44.71979 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 343176f7-9791-3ac5-a915-02c6a3db5b28 | -18.32893 | -42.37491 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0d083f15-1cb0-3d34-9892-0cb7791881b6 | -14.01227 | -41.84722 | 2026-10-09 15:58:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 95150535-03db-3d5f-b554-f188485b34d5 | -18.78835 | -46.47361 | 2026-10-09 15:58:00 | NPP-375 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8b0d0022-f955-34cc-863d-9ab8bae08210 | -11.82739 | -43.59872 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0284d161-eaf1-3be4-9104-81ab58a6b09b | -16.96787 | -41.15482 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| d0a90254-0b33-3075-90e6-2ffcf3ab8428 | -11.9911 | -43.48824 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f5d91bd6-374e-3179-ac1d-a5e32c225f87 | -15.11075 | -43.63515 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7911ef97-8e2c-36ab-98b2-f2e8f9c5a650 | -12.24712 | -44.76094 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9140ac13-36d9-36f4-837f-f4a5f11cbbe9 | -14.43599 | -43.93709 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c8d16865-5ab8-3fd8-9a62-74e932ba8865 | -15.4839 | -41.21656 | 2026-10-09 15:58:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b833fda8-dabf-360e-b9dc-8aa3b3274389 | -11.98317 | -43.46978 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4f69afec-1e30-30ec-a9d7-e9a6a95be139 | -13.29139 | -46.97114 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38dd31a1-27ed-3a38-9234-355428c6169f | -13.28605 | -40.32956 | 2026-10-09 15:58:00 | NPP-375 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 27422421-7063-37af-97c9-e3cfa876e25d | -15.37146 | -44.83148 | 2026-10-09 15:58:00 | NPP-375 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 903574d2-d574-36c8-87b4-80dce02b3ddf | -17.09755 | -40.76524 | 2026-10-09 15:58:00 | NPP-375 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c3f1c182-f28a-3b94-b555-2733c7f4bd7f | -15.37255 | -44.84217 | 2026-10-09 15:58:00 | NPP-375 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6138ed14-c582-35ff-ad71-1d535eee6ad0 | -11.62191 | -43.60153 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7a22d5c8-4de4-3aa3-b580-f80836f48f43 | -11.57582 | -42.80838 | 2026-10-09 15:58:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| c95929eb-b18d-355a-a25c-80a4e4d062b4 | -12.01462 | -43.44151 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4c6070ca-fb44-3093-9bce-ad5f11d47661 | -12.29831 | -47.06485 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| edc86cf0-2927-3d5c-9489-c714644e72bd | -14.64757 | -43.52668 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| d8ad21d7-3b08-3922-ab0f-8dc064e0bb65 | -14.05419 | -44.78605 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 91390aa3-a904-3c84-91bf-b33fc320fc84 | -14.38867 | -42.82093 | 2026-10-09 15:58:00 | NPP-375 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7e3df8a0-0e65-3ac7-bee5-317f827fbaeb | -17.40493 | -39.60014 | 2026-10-09 15:58:00 | NPP-375 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 502b1442-982b-37a0-8e40-0a9242f6c3cb | -12.22232 | -44.75229 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 13c9c4da-593e-34ea-b1b0-4f006fc5cf92 | -11.99148 | -43.49157 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e30c51b9-e42b-3d11-a907-429f5fd8b8f2 | -11.59358 | -43.70778 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7fb5acde-0331-3782-8306-a65280b5be05 | -15.79775 | -39.52761 | 2026-10-09 15:58:00 | NPP-375 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 127499ac-c4cc-3ace-a38c-92dd4347edfb | -15.37997 | -41.92789 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 3e766507-0397-3f2e-a430-c03d374d7807 | -16.11746 | -42.85384 | 2026-10-09 15:58:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ead352a1-1aa3-391e-a674-6d86da1686cc | -16.23964 | -42.53245 | 2026-10-09 15:58:00 | NPP-375 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fd399df-0016-3677-8977-365912094efc | -14.54636 | -44.90377 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 108b4002-355d-3a31-9f1a-a78840a31697 | -11.66118 | -43.68544 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| f26dbe21-cd8a-3e2d-a30a-cb047f866ac8 | -11.97154 | -43.47882 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d3cba18b-6b38-3bad-bce1-79fa39ada0e1 | -11.98675 | -43.46099 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c6127fdc-d1a9-30b4-9601-300fcc26f743 | -14.32999 | -41.30208 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 126.7 |
| fda5a1da-21c9-355d-b217-982bf4e625c4 | -11.89462 | -47.40052 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bf80832f-8062-3c38-98f0-d799ccbc7054 | -14.48007 | -40.45292 | 2026-10-09 15:58:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 562e9e8d-fd89-3988-90c4-70cf325cdc12 | -12.81867 | -44.66042 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1e8d9bad-1f0d-3352-8d72-52918a79a55e | -15.37201 | -44.83684 | 2026-10-09 15:58:00 | NPP-375 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5b97e0b1-f86e-39d5-9615-f577beb32e9d | -11.60612 | -43.61563 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 078e6925-eb5b-3a26-90ac-0adb2fbb1844 | -15.11724 | -43.63899 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 04c610fe-c6f8-3387-9d12-c7b30d2e15bf | -11.60697 | -43.6277 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8fa6eb5e-6cab-3ad1-8532-c0f525f2eacd | -15.25675 | -42.36124 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| 7e1f1d29-a5a0-3d4a-ac52-f9ad0776c1cd | -11.58111 | -43.65088 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 38954524-58ca-380b-abe4-23e595a63c40 | -14.06039 | -43.83675 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| fa2c8302-06e1-3107-ba5c-611175495b34 | -11.9889 | -43.46929 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 08cd3979-2bd8-3acb-9d34-03157379232c | -12.15847 | -44.74451 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1bfdc0-14d4-33e4-b65b-e50135f8ea7e | -13.56121 | -40.896 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 341f2778-6823-3c68-b31f-26e4abd0865a | -16.2708 | -44.17064 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 61b5000b-74d0-3f90-8281-923e0af5f269 | -11.57692 | -43.66763 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 829a368c-26ce-3b1c-92ae-d2a8079a7c05 | -11.60366 | -43.69476 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8e0c39ec-5403-36ab-8a76-a1e14bbbd884 | -18.32958 | -42.37119 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8fd2056c-5ef2-372b-8191-6adc42e22dfc | -12.22291 | -44.75729 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6027210b-6c6e-3cfd-9fbd-d1b00847a13c | -10.80271 | -39.36547 | 2026-10-09 15:58:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |


[Clique aqui para ver as próximas entradas](README267.md)
